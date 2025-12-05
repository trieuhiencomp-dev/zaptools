/**
 * Azure TTS Integration - FREE TIER
 *
 * Free Tier: 5 million characters/month
 * Docs: https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/
 */

const fetch = require('node-fetch');
const crypto = require('crypto');

class AzureTTS {
    constructor() {
        // IMPORTANT: Get free key from https://portal.azure.com
        // 1. Create "Speech" resource (FREE tier)
        // 2. Copy key and region
        this.subscriptionKey = process.env.AZURE_TTS_KEY || 'YOUR_FREE_AZURE_KEY';
        this.region = process.env.AZURE_TTS_REGION || 'southeastasia'; // Closest to Vietnam
        this.endpoint = `https://${this.region}.tts.speech.microsoft.com/cognitiveservices/v1`;
    }

    /**
     * Generate hash for caching
     */
    generateHash(text, voice) {
        return crypto
            .createHash('md5')
            .update(text + voice)
            .digest('hex');
    }

    /**
     * Convert text to speech using Azure
     *
     * @param {string} text - Text to convert (max 1000 chars)
     * @param {string} voice - Voice name (default: vi-VN-HoaiMyNeural)
     * @returns {Promise<Buffer>} - Audio buffer (MP3)
     */
    async textToSpeech(text, voice = 'vi-VN-HoaiMyNeural') {
        // Validate input
        if (!text || text.length === 0) {
            throw new Error('Text is required');
        }

        if (text.length > 1000) {
            throw new Error('Text too long (max 1000 characters)');
        }

        // Build SSML (Speech Synthesis Markup Language)
        const ssml = this.buildSSML(text, voice);

        try {
            const response = await fetch(this.endpoint, {
                method: 'POST',
                headers: {
                    'Ocp-Apim-Subscription-Key': this.subscriptionKey,
                    'Content-Type': 'application/ssml+xml',
                    'X-Microsoft-OutputFormat': 'audio-16khz-128kbitrate-mono-mp3',
                    'User-Agent': 'ZapTools-TTS'
                },
                body: ssml
            });

            if (!response.ok) {
                const error = await response.text();
                throw new Error(`Azure TTS API error: ${response.status} - ${error}`);
            }

            // Return audio buffer
            const audioBuffer = await response.buffer();
            return audioBuffer;

        } catch (error) {
            console.error('Azure TTS Error:', error);
            throw error;
        }
    }

    /**
     * Build SSML markup
     */
    buildSSML(text, voice) {
        // Escape XML special characters
        const escapedText = text
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&apos;');

        return `
            <speak version='1.0' xml:lang='vi-VN'>
                <voice name='${voice}'>
                    ${escapedText}
                </voice>
            </speak>
        `.trim();
    }

    /**
     * Get available Vietnamese voices
     */
    getAvailableVoices() {
        return [
            {
                name: 'vi-VN-HoaiMyNeural',
                displayName: 'Hoài My (Nữ - Tự nhiên)',
                gender: 'Female',
                type: 'Neural',
                free: true
            },
            {
                name: 'vi-VN-NamMinhNeural',
                displayName: 'Nam Minh (Nam - Tự nhiên)',
                gender: 'Male',
                type: 'Neural',
                free: true
            }
        ];
    }

    /**
     * Calculate character usage (for monitoring free tier)
     */
    getCharacterCount(text) {
        return text.length;
    }
}

module.exports = AzureTTS;
