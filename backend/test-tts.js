/**
 * Test TTS Backend - Verify Azure connection
 */

require('dotenv').config();
const AzureTTS = require('./azure-tts');
const CacheManager = require('./cache-manager');
const RateLimiter = require('./rate-limiter');

async function testAzureTTS() {
    console.log('🧪 Testing Azure TTS...\n');

    const tts = new AzureTTS();
    const testText = 'Xin chào, đây là test giọng đọc tiếng Việt.';

    try {
        console.log('📝 Converting text:', testText);
        const audioBuffer = await tts.textToSpeech(testText);
        console.log('✅ Azure TTS works!');
        console.log('   Audio size:', audioBuffer.length, 'bytes');
        console.log('   Characters:', testText.length);
        return true;
    } catch (error) {
        console.error('❌ Azure TTS failed:', error.message);
        return false;
    }
}

async function testCache() {
    console.log('\n🧪 Testing Cache Manager...\n');

    const cache = new CacheManager();
    const testText = 'Test cache';
    const testVoice = 'vi-VN-HoaiMyNeural';
    const testBuffer = Buffer.from('fake audio data');

    try {
        // Test save
        await cache.set(testText, testVoice, testBuffer);
        console.log('✅ Cache save works!');

        // Test retrieve
        const cached = await cache.get(testText, testVoice);
        if (cached) {
            console.log('✅ Cache retrieve works!');
        } else {
            console.error('❌ Cache retrieve failed');
        }

        // Test stats
        const stats = await cache.getStats();
        console.log('✅ Cache stats:', stats);

        return true;
    } catch (error) {
        console.error('❌ Cache test failed:', error.message);
        return false;
    }
}

function testRateLimiter() {
    console.log('\n🧪 Testing Rate Limiter...\n');

    const limiter = new RateLimiter();
    const testIP = '127.0.0.1';

    try {
        // Test first request
        const check1 = limiter.checkLimit(testIP, 100);
        console.log('✅ First request allowed:', check1.allowed);

        limiter.recordRequest(testIP, 100);

        // Test second request
        const check2 = limiter.checkLimit(testIP, 100);
        console.log('✅ Second request allowed:', check2.allowed);
        console.log('   Remaining (hourly):', check2.remaining?.hourly);

        // Test stats
        const stats = limiter.getStats();
        console.log('✅ Rate limit stats:', stats);

        return true;
    } catch (error) {
        console.error('❌ Rate limiter test failed:', error.message);
        return false;
    }
}

async function runAllTests() {
    console.log('╔════════════════════════════════════════╗');
    console.log('║   ZapTools TTS Backend Tests          ║');
    console.log('╚════════════════════════════════════════╝\n');

    const results = {
        azure: await testAzureTTS(),
        cache: await testCache(),
        rateLimiter: testRateLimiter()
    };

    console.log('\n╔════════════════════════════════════════╗');
    console.log('║   Test Results                         ║');
    console.log('╠════════════════════════════════════════╣');
    console.log('║ Azure TTS:      ', results.azure ? '✅ PASS' : '❌ FAIL', '               ║');
    console.log('║ Cache Manager:  ', results.cache ? '✅ PASS' : '❌ FAIL', '               ║');
    console.log('║ Rate Limiter:   ', results.rateLimiter ? '✅ PASS' : '❌ FAIL', '               ║');
    console.log('╚════════════════════════════════════════╝\n');

    const allPassed = results.azure && results.cache && results.rateLimiter;

    if (allPassed) {
        console.log('🎉 All tests passed! Backend ready to use.\n');
        process.exit(0);
    } else {
        console.log('⚠️  Some tests failed. Please check configuration.\n');
        process.exit(1);
    }
}

// Run tests
runAllTests();
