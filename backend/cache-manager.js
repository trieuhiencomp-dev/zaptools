/**
 * Cache Manager - File-based (FREE - No Redis needed)
 *
 * Strategy: Cache MP3 files to reduce Azure API calls
 * Goal: 70-80% cache hit rate = Stay in FREE tier!
 */

const fs = require('fs').promises;
const path = require('path');
const crypto = require('crypto');

class CacheManager {
    constructor() {
        this.cacheDir = path.join(__dirname, '../cache/tts');
        this.statsFile = path.join(__dirname, '../cache/stats.json');
        this.maxCacheSize = 500; // Max 500 MB cache
        this.cacheDuration = 30 * 24 * 60 * 60 * 1000; // 30 days

        this.initCache();
    }

    /**
     * Initialize cache directory
     */
    async initCache() {
        try {
            await fs.mkdir(this.cacheDir, { recursive: true });
            console.log('✅ Cache directory ready:', this.cacheDir);
        } catch (error) {
            console.error('Cache init error:', error);
        }
    }

    /**
     * Generate cache key from text + voice
     */
    getCacheKey(text, voice) {
        const hash = crypto
            .createHash('md5')
            .update(`${text}_${voice}`)
            .digest('hex');
        return hash;
    }

    /**
     * Get cached audio file
     *
     * @param {string} text
     * @param {string} voice
     * @returns {Promise<Buffer|null>} - Audio buffer or null if not cached
     */
    async get(text, voice) {
        const key = this.getCacheKey(text, voice);
        const filePath = path.join(this.cacheDir, `${key}.mp3`);

        try {
            // Check if file exists
            const stats = await fs.stat(filePath);

            // Check if cache expired (30 days)
            const age = Date.now() - stats.mtime.getTime();
            if (age > this.cacheDuration) {
                console.log('⏰ Cache expired:', key);
                await this.delete(key);
                await this.logStats('expired', text.length);
                return null;
            }

            // Read cached file
            const buffer = await fs.readFile(filePath);
            console.log('✅ Cache HIT:', key, `(${text.length} chars saved)`);
            await this.logStats('hit', text.length);
            return buffer;

        } catch (error) {
            // File not found = cache miss
            console.log('❌ Cache MISS:', key);
            await this.logStats('miss', text.length);
            return null;
        }
    }

    /**
     * Save audio to cache
     *
     * @param {string} text
     * @param {string} voice
     * @param {Buffer} audioBuffer
     */
    async set(text, voice, audioBuffer) {
        const key = this.getCacheKey(text, voice);
        const filePath = path.join(this.cacheDir, `${key}.mp3`);

        try {
            await fs.writeFile(filePath, audioBuffer);
            console.log('💾 Cached:', key, `(${audioBuffer.length} bytes)`);

            // Clean old cache if needed
            await this.cleanOldCache();

        } catch (error) {
            console.error('Cache save error:', error);
        }
    }

    /**
     * Delete cached file
     */
    async delete(key) {
        const filePath = path.join(this.cacheDir, `${key}.mp3`);
        try {
            await fs.unlink(filePath);
        } catch (error) {
            // Ignore if file doesn't exist
        }
    }

    /**
     * Clean old cache files (LRU - Least Recently Used)
     */
    async cleanOldCache() {
        try {
            const files = await fs.readdir(this.cacheDir);

            // Get file stats
            const fileStats = await Promise.all(
                files.map(async (file) => {
                    const filePath = path.join(this.cacheDir, file);
                    const stats = await fs.stat(filePath);
                    return {
                        file,
                        path: filePath,
                        atime: stats.atime.getTime(),
                        size: stats.size
                    };
                })
            );

            // Calculate total cache size
            const totalSize = fileStats.reduce((sum, f) => sum + f.size, 0);
            const totalSizeMB = totalSize / (1024 * 1024);

            console.log(`📦 Cache size: ${totalSizeMB.toFixed(2)} MB`);

            // If cache too large, delete oldest files
            if (totalSizeMB > this.maxCacheSize) {
                console.log('🧹 Cleaning old cache...');

                // Sort by access time (oldest first)
                fileStats.sort((a, b) => a.atime - b.atime);

                // Delete oldest 20%
                const toDelete = Math.ceil(fileStats.length * 0.2);
                for (let i = 0; i < toDelete; i++) {
                    await fs.unlink(fileStats[i].path);
                    console.log('🗑️ Deleted:', fileStats[i].file);
                }
            }

        } catch (error) {
            console.error('Cache clean error:', error);
        }
    }

    /**
     * Log cache statistics (for monitoring FREE tier usage)
     */
    async logStats(type, charCount) {
        try {
            let stats = { hit: 0, miss: 0, expired: 0, charsSaved: 0, charsUsed: 0 };

            // Read existing stats
            try {
                const data = await fs.readFile(this.statsFile, 'utf8');
                stats = JSON.parse(data);
            } catch (error) {
                // File doesn't exist yet
            }

            // Update stats
            stats[type] = (stats[type] || 0) + 1;

            if (type === 'hit') {
                stats.charsSaved = (stats.charsSaved || 0) + charCount;
            } else if (type === 'miss') {
                stats.charsUsed = (stats.charsUsed || 0) + charCount;
            }

            // Calculate hit rate
            const total = stats.hit + stats.miss;
            stats.hitRate = total > 0 ? ((stats.hit / total) * 100).toFixed(2) + '%' : '0%';

            // Save stats
            await fs.writeFile(this.statsFile, JSON.stringify(stats, null, 2));

        } catch (error) {
            console.error('Stats logging error:', error);
        }
    }

    /**
     * Get cache statistics
     */
    async getStats() {
        try {
            const data = await fs.readFile(this.statsFile, 'utf8');
            const stats = JSON.parse(data);

            // Add free tier info
            const freeTierLimit = 5000000; // 5M chars/month
            const remaining = freeTierLimit - stats.charsUsed;
            const percentUsed = ((stats.charsUsed / freeTierLimit) * 100).toFixed(2);

            return {
                ...stats,
                freeTier: {
                    limit: freeTierLimit,
                    used: stats.charsUsed,
                    remaining: remaining,
                    percentUsed: percentUsed + '%',
                    status: remaining > 0 ? '✅ FREE' : '⚠️ EXCEEDED'
                }
            };

        } catch (error) {
            return null;
        }
    }

    /**
     * Clear all cache
     */
    async clearAll() {
        try {
            const files = await fs.readdir(this.cacheDir);
            await Promise.all(
                files.map(file => fs.unlink(path.join(this.cacheDir, file)))
            );
            console.log('🗑️ All cache cleared');
        } catch (error) {
            console.error('Clear cache error:', error);
        }
    }
}

module.exports = CacheManager;
