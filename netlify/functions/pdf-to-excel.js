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

    // Create conversion job
    const job = await cloudConvert.jobs.create({
      tasks: {
        'import-pdf': {
          operation: 'import/base64',
          file: file,
          filename: filename || 'input.pdf'
        },
        'convert-to-xlsx': {
          operation: 'convert',
          input: 'import-pdf',
          output_format: 'xlsx',
          engine: 'office'
        },
        'export-xlsx': {
          operation: 'export/url',
          input: 'convert-to-xlsx'
        }
      }
    });

    // Wait for job to complete
    const completedJob = await cloudConvert.jobs.wait(job.id);

    // Get the export task
    const exportTask = completedJob.tasks.find(task => task.name === 'export-xlsx');

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
        'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'Content-Disposition': `attachment; filename="${filename.replace('.pdf', '.xlsx')}"`
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
