/**
 * TTS API - Main Entry Point
 *
 * Combines: Azure TTS + Cache + Rate Limiting
 * Goal: 100% FREE (stay in Azure free tier)
 */

// Load environment variables from .env file
require('dotenv').config();

const express = require('express');
const cors = require('cors');
const AzureTTS = require('./azure-tts');
const CacheManager = require('./cache-manager');
const RateLimiter = require('./rate-limiter');

const app = express();
const PORT = process.env.PORT || 3000;

// Initialize services
const azureTTS = new AzureTTS();
const cache = new CacheManager();
const rateLimiter = new RateLimiter();

// Middleware
app.use(cors());
app.use(express.json());

// Serve cached MP3 files at /cache/tts path
const path = require('path');
app.use('/cache', express.static(path.join(__dirname, '../cache')));

/**
 * Get client IP address
 */
function getClientIP(req) {
    return req.headers['x-forwarded-for']?.split(',')[0] ||
           req.headers['x-real-ip'] ||
           req.connection.remoteAddress ||
           'unknown';
}

/**
 * POST /api/tts/convert
 *
 * Convert text to speech
 *
 * Body: {
 *   text: string (max 1000 chars),
 *   voice: string (optional)
 * }
 */
app.post('/api/tts/convert', async (req, res) => {
    const { text, voice = 'vi-VN-HoaiMyNeural' } = req.body;
    const clientIP = getClientIP(req);

    console.log(`🎙️ TTS Request from ${clientIP}: ${text.substring(0, 50)}...`);

    try {
        // Validate input
        if (!text || typeof text !== 'string') {
            return res.status(400).json({
                success: false,
                error: 'Text is required'
            });
        }

        const charCount = text.length;

        // Check rate limit
        const rateCheck = rateLimiter.checkLimit(clientIP, charCount);
        if (!rateCheck.allowed) {
            return res.status(429).json({
                success: false,
                error: rateCheck.reason,
                limit: rateCheck.limit,
                current: rateCheck.current,
                waitMinutes: rateCheck.waitMinutes,
                resetHours: rateCheck.resetHours
            });
        }

        // Check cache first
        let audioBuffer = await cache.get(text, voice);

        if (audioBuffer) {
            // Cache HIT - Free!
            console.log('✅ Serving from cache (FREE)');

            // Record request (for stats)
            rateLimiter.recordRequest(clientIP, charCount);

            // Return cached audio
            const cacheKey = cache.getCacheKey(text, voice);
            return res.json({
                success: true,
                fromCache: true,
                audioUrl: `/cache/tts/${cacheKey}.mp3`,
                charCount: charCount,
                remaining: rateCheck.remaining,
                message: 'Converted successfully (from cache)'
            });

        } else {
            // Cache MISS - Call Azure API (uses free tier quota)
            console.log('⚡ Calling Azure TTS API...');

            audioBuffer = await azureTTS.textToSpeech(text, voice);

            // Save to cache for future use
            await cache.set(text, voice, audioBuffer);

            // Record request
            rateLimiter.recordRequest(clientIP, charCount);

            // Return audio URL
            const cacheKey = cache.getCacheKey(text, voice);
            return res.json({
                success: true,
                fromCache: false,
                audioUrl: `/cache/tts/${cacheKey}.mp3`,
                charCount: charCount,
                remaining: rateCheck.remaining,
                message: 'Converted successfully'
            });
        }

    } catch (error) {
        console.error('❌ TTS Error:', error);

        return res.status(500).json({
            success: false,
            error: 'Conversion failed. Please try again.',
            details: process.env.NODE_ENV === 'development' ? error.message : undefined
        });
    }
});

/**
 * GET /api/tts/voices
 *
 * Get available Vietnamese voices
 */
app.get('/api/tts/voices', (req, res) => {
    const voices = azureTTS.getAvailableVoices();
    res.json({
        success: true,
        voices: voices
    });
});

/**
 * GET /api/tts/stats
 *
 * Get cache and usage statistics (Admin only)
 */
app.get('/api/tts/stats', async (req, res) => {
    try {
        const cacheStats = await cache.getStats();
        const rateLimitStats = rateLimiter.getStats();

        res.json({
            success: true,
            cache: cacheStats,
            rateLimit: rateLimitStats,
            timestamp: new Date().toISOString()
        });

    } catch (error) {
        res.status(500).json({
            success: false,
            error: 'Failed to get stats'
        });
    }
});

/**
 * POST /api/tts/cache/clear (Admin only - add authentication in production!)
 *
 * Clear all cache
 */
app.post('/api/tts/cache/clear', async (req, res) => {
    const { adminKey } = req.body;

    // Simple admin key check (use proper auth in production!)
    if (adminKey !== process.env.ADMIN_KEY) {
        return res.status(403).json({
            success: false,
            error: 'Unauthorized'
        });
    }

    try {
        await cache.clearAll();
        res.json({
            success: true,
            message: 'Cache cleared successfully'
        });
    } catch (error) {
        res.status(500).json({
            success: false,
            error: 'Failed to clear cache'
        });
    }
});

/**
 * Health check
 */
app.get('/health', (req, res) => {
    res.json({
        status: 'ok',
        service: 'ZapTools TTS API',
        version: '1.0.0',
        timestamp: new Date().toISOString()
    });
});

/**
 * Start server
 */
app.listen(PORT, () => {
    console.log(`
╔════════════════════════════════════════╗
║   ZapTools TTS API - FREE TIER        ║
║   🎙️  Azure Cognitive Services        ║
║   💾  File-based caching              ║
║   🛡️  Rate limiting enabled            ║
╚════════════════════════════════════════╝

✅ Server running on http://localhost:${PORT}
✅ FREE tier: 5M chars/month
✅ Cache hit rate target: 70-80%

Endpoints:
  POST   /api/tts/convert        - Convert text to speech
  GET    /api/tts/voices         - Get available voices
  GET    /api/tts/stats          - Get usage stats
  GET    /health                 - Health check
    `);
});

module.exports = app;
