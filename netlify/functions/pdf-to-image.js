const CloudConvert = require('cloudconvert');
const fetch = require('node-fetch');

exports.handler = async (event, context) => {
  // Only allow POST requests
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ error: 'Method not allowed' })
    };
  }

  try {
    const CLOUDCONVERT_API_KEY = process.env.CLOUDCONVERT_API_KEY;

    if (!CLOUDCONVERT_API_KEY) {
      throw new Error('CloudConvert API key not configured');
    }

    // Parse base64 encoded file from request body
    const { file, filename } = JSON.parse(event.body);

    if (!file) {
      return {
        statusCode: 400,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ error: 'No file provided' })
      };
    }

    // Initialize CloudConvert client
    const cloudConvert = new CloudConvert(CLOUDCONVERT_API_KEY);

    // Create conversion job (convert PDF to PNG and create ZIP archive)
    const job = await cloudConvert.jobs.create({
      tasks: {
        'import-pdf': {
          operation: 'import/base64',
          file: file,
          filename: filename || 'input.pdf'
        },
        'convert-to-png': {
          operation: 'convert',
          input: 'import-pdf',
          output_format: 'png',
          pages: 'all', // Convert all pages
          engine: 'imagemagick'
        },
        'create-archive': {
          operation: 'archive',
          input: ['convert-to-png'],
          output_format: 'zip'
        },
        'export-zip': {
          operation: 'export/url',
          input: 'create-archive'
        }
      }
    });

    // Wait for job to complete
    const completedJob = await cloudConvert.jobs.wait(job.id);

    // Get the export task
    const exportTask = completedJob.tasks.find(task => task.name === 'export-zip');

    if (!exportTask || !exportTask.result || !exportTask.result.files || exportTask.result.files.length === 0) {
      throw new Error('Conversion failed - no output file');
    }

    // Download the converted file
    const file_url = exportTask.result.files[0].url;
    const fileResponse = await fetch(file_url);
    const fileBuffer = await fileResponse.buffer();

    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/zip',
        'Content-Disposition': `attachment; filename="images.zip"`
      },
      body: fileBuffer.toString('base64'),
      isBase64Encoded: true
    };

  } catch (error) {
    console.error('Conversion error:', error);
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        error: error.message || 'Conversion failed',
        details: error.toString()
      })
    };
  }
};
