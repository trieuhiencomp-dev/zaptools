/**
 * ZapTools - Tool Usage Logger
 * Monitors tool performance, errors, and user experience
 * Last updated: December 2025
 */

class ToolUsageLogger {
    constructor(toolName) {
        this.toolName = toolName;
        this.sessionId = this.generateSessionId();
        this.logs = [];
    }

    generateSessionId() {
        return `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
    }

    logEvent(eventType, data = {}) {
        const logEntry = {
            timestamp: new Date().toISOString(),
            sessionId: this.sessionId,
            toolName: this.toolName,
            eventType: eventType,
            userAgent: navigator.userAgent,
            language: navigator.language,
            ...data
        };

        this.logs.push(logEntry);

        // Store in localStorage for later review
        this.saveToLocalStorage(logEntry);

        // Console log for debugging
        if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            console.log('[ToolLogger]', logEntry);
        }
    }

    saveToLocalStorage(logEntry) {
        try {
            const storageKey = 'zaptools_usage_logs';
            let existingLogs = JSON.parse(localStorage.getItem(storageKey) || '[]');

            // Keep only last 100 logs to prevent storage overflow
            if (existingLogs.length >= 100) {
                existingLogs = existingLogs.slice(-50);
            }

            existingLogs.push(logEntry);
            localStorage.setItem(storageKey, JSON.stringify(existingLogs));
        } catch (error) {
            console.warn('Failed to save log to localStorage:', error);
        }
    }

    // Tool lifecycle events
    logToolLoad() {
        this.logEvent('TOOL_LOAD', {
            url: window.location.href,
            referrer: document.referrer
        });
    }

    logFileSelection(fileName, fileSize, fileType) {
        this.logEvent('FILE_SELECTED', {
            fileName: fileName,
            fileSize: fileSize,
            fileType: fileType
        });
    }

    logConversionStart(inputFormat, outputFormat) {
        this.conversionStartTime = Date.now();
        this.logEvent('CONVERSION_START', {
            inputFormat: inputFormat,
            outputFormat: outputFormat
        });
    }

    logConversionSuccess(outputFileName) {
        const duration = Date.now() - this.conversionStartTime;
        this.logEvent('CONVERSION_SUCCESS', {
            duration: duration,
            outputFileName: outputFileName
        });
    }

    logConversionError(errorMessage, errorType = 'UNKNOWN') {
        const duration = this.conversionStartTime ? Date.now() - this.conversionStartTime : 0;
        this.logEvent('CONVERSION_ERROR', {
            duration: duration,
            errorMessage: errorMessage,
            errorType: errorType
        });
    }

    logDownload(fileName) {
        this.logEvent('FILE_DOWNLOAD', {
            fileName: fileName
        });
    }

    logUserFeedback(rating, comment = '') {
        this.logEvent('USER_FEEDBACK', {
            rating: rating,
            comment: comment
        });
    }

    logToolExit(timeSpent) {
        this.logEvent('TOOL_EXIT', {
            timeSpent: timeSpent,
            totalLogs: this.logs.length
        });
    }

    // Get aggregated statistics
    static getUsageStatistics() {
        try {
            const logs = JSON.parse(localStorage.getItem('zaptools_usage_logs') || '[]');

            const stats = {
                totalSessions: new Set(logs.map(log => log.sessionId)).size,
                totalConversions: logs.filter(log => log.eventType === 'CONVERSION_SUCCESS').length,
                totalErrors: logs.filter(log => log.eventType === 'CONVERSION_ERROR').length,
                avgConversionTime: 0,
                toolUsageBreakdown: {},
                errorTypes: {},
                successRate: 0
            };

            // Calculate average conversion time
            const successfulConversions = logs.filter(log => log.eventType === 'CONVERSION_SUCCESS');
            if (successfulConversions.length > 0) {
                stats.avgConversionTime = successfulConversions.reduce((sum, log) => sum + (log.duration || 0), 0) / successfulConversions.length;
            }

            // Tool usage breakdown
            logs.forEach(log => {
                if (!stats.toolUsageBreakdown[log.toolName]) {
                    stats.toolUsageBreakdown[log.toolName] = 0;
                }
                if (log.eventType === 'CONVERSION_SUCCESS') {
                    stats.toolUsageBreakdown[log.toolName]++;
                }
            });

            // Error types
            logs.filter(log => log.eventType === 'CONVERSION_ERROR').forEach(log => {
                const errorType = log.errorType || 'UNKNOWN';
                stats.errorTypes[errorType] = (stats.errorTypes[errorType] || 0) + 1;
            });

            // Success rate
            const totalAttempts = stats.totalConversions + stats.totalErrors;
            stats.successRate = totalAttempts > 0 ? ((stats.totalConversions / totalAttempts) * 100).toFixed(2) : 0;

            return stats;
        } catch (error) {
            console.error('Failed to get usage statistics:', error);
            return null;
        }
    }

    // Export logs for analysis
    static exportLogs() {
        try {
            const logs = JSON.parse(localStorage.getItem('zaptools_usage_logs') || '[]');
            const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(logs, null, 2));
            const downloadAnchor = document.createElement('a');
            downloadAnchor.setAttribute("href", dataStr);
            downloadAnchor.setAttribute("download", `zaptools_logs_${Date.now()}.json`);
            document.body.appendChild(downloadAnchor);
            downloadAnchor.click();
            downloadAnchor.remove();
            return true;
        } catch (error) {
            console.error('Failed to export logs:', error);
            return false;
        }
    }

    // Clear old logs
    static clearLogs() {
        try {
            localStorage.removeItem('zaptools_usage_logs');
            return true;
        } catch (error) {
            console.error('Failed to clear logs:', error);
            return false;
        }
    }
}

// Auto-initialize logger when page loads
window.addEventListener('DOMContentLoaded', function() {
    // Get tool name from page title or URL
    const toolName = document.title.split('-')[0].trim() || window.location.pathname.split('/').pop().replace('.html', '');
    window.toolLogger = new ToolUsageLogger(toolName);
    window.toolLogger.logToolLoad();

    // Track time spent on page
    const pageLoadTime = Date.now();
    window.addEventListener('beforeunload', function() {
        const timeSpent = Date.now() - pageLoadTime;
        window.toolLogger.logToolExit(timeSpent);
    });
});

// Make it globally accessible
window.ToolUsageLogger = ToolUsageLogger;
