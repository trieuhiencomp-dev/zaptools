/**
 * Rate Limiter - Prevent abuse and stay in FREE tier
 *
 * Limits:
 * - 10 requests per hour per IP
 * - 1000 chars per request
 * - Max 50 requests per day per IP
 */

class RateLimiter {
    constructor() {
        // In-memory store (for simple implementation)
        // For production, use Redis or database
        this.requests = new Map(); // IP -> [{timestamp, charCount}]
        this.cleanupInterval = 60 * 60 * 1000; // Clean every 1 hour

        this.limits = {
            requestsPerHour: 10,
            requestsPerDay: 50,
            maxCharsPerRequest: 1000
        };

        // Auto cleanup old records
        setInterval(() => this.cleanup(), this.cleanupInterval);
    }

    /**
     * Check if request is allowed
     *
     * @param {string} ip - User IP address
     * @param {number} charCount - Text character count
     * @returns {Object} - {allowed: boolean, reason: string}
     */
    checkLimit(ip, charCount) {
        const now = Date.now();
        const oneHourAgo = now - (60 * 60 * 1000);
        const oneDayAgo = now - (24 * 60 * 60 * 1000);

        // Get user's request history
        const userRequests = this.requests.get(ip) || [];

        // Filter recent requests
        const recentRequests = userRequests.filter(r => r.timestamp > oneHourAgo);
        const todayRequests = userRequests.filter(r => r.timestamp > oneDayAgo);

        // Check character limit
        if (charCount > this.limits.maxCharsPerRequest) {
            return {
                allowed: false,
                reason: `Text too long. Max ${this.limits.maxCharsPerRequest} characters allowed.`,
                limit: this.limits.maxCharsPerRequest,
                current: charCount
            };
        }

        // Check hourly limit
        if (recentRequests.length >= this.limits.requestsPerHour) {
            const oldestRequest = recentRequests[0];
            const waitTime = Math.ceil((oldestRequest.timestamp + (60 * 60 * 1000) - now) / 60000);

            return {
                allowed: false,
                reason: `Rate limit exceeded. Please wait ${waitTime} minutes.`,
                limit: this.limits.requestsPerHour,
                current: recentRequests.length,
                waitMinutes: waitTime
            };
        }

        // Check daily limit
        if (todayRequests.length >= this.limits.requestsPerDay) {
            const hoursUntilReset = Math.ceil((todayRequests[0].timestamp + (24 * 60 * 60 * 1000) - now) / (60 * 60 * 1000));

            return {
                allowed: false,
                reason: `Daily limit reached. Resets in ${hoursUntilReset} hours.`,
                limit: this.limits.requestsPerDay,
                current: todayRequests.length,
                resetHours: hoursUntilReset
            };
        }

        // Request allowed
        return {
            allowed: true,
            remaining: {
                hourly: this.limits.requestsPerHour - recentRequests.length,
                daily: this.limits.requestsPerDay - todayRequests.length
            }
        };
    }

    /**
     * Record a request
     */
    recordRequest(ip, charCount) {
        const userRequests = this.requests.get(ip) || [];

        userRequests.push({
            timestamp: Date.now(),
            charCount: charCount
        });

        this.requests.set(ip, userRequests);

        console.log(`📊 Rate limit - IP: ${ip}, Requests: ${userRequests.length}, Chars: ${charCount}`);
    }

    /**
     * Cleanup old request records
     */
    cleanup() {
        const oneDayAgo = Date.now() - (24 * 60 * 60 * 1000);

        for (const [ip, requests] of this.requests.entries()) {
            // Filter out requests older than 24 hours
            const recentRequests = requests.filter(r => r.timestamp > oneDayAgo);

            if (recentRequests.length === 0) {
                // No recent requests, remove IP
                this.requests.delete(ip);
            } else {
                // Update with filtered requests
                this.requests.set(ip, recentRequests);
            }
        }

        console.log(`🧹 Rate limiter cleanup: ${this.requests.size} IPs tracked`);
    }

    /**
     * Get statistics
     */
    getStats() {
        const now = Date.now();
        const oneHourAgo = now - (60 * 60 * 1000);

        let totalRequests = 0;
        let activeUsers = 0;

        for (const requests of this.requests.values()) {
            totalRequests += requests.length;
            const recentRequests = requests.filter(r => r.timestamp > oneHourAgo);
            if (recentRequests.length > 0) activeUsers++;
        }

        return {
            totalIPs: this.requests.size,
            activeUsersLastHour: activeUsers,
            totalRequests: totalRequests,
            limits: this.limits
        };
    }

    /**
     * Clear all rate limit data (admin only)
     */
    clearAll() {
        this.requests.clear();
        console.log('🗑️ All rate limit data cleared');
    }
}

module.exports = RateLimiter;
