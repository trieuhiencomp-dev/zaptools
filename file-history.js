// File History Feature with localStorage
(function() {
    'use strict';

    const MAX_HISTORY = 5;
    const HISTORY_KEY = 'zaptools_file_history';

    // Get file history from localStorage
    function getHistory() {
        try {
            const history = localStorage.getItem(HISTORY_KEY);
            return history ? JSON.parse(history) : [];
        } catch (e) {
            console.error('Error reading history:', e);
            return [];
        }
    }

    // Save file to history
    function addToHistory(fileName, toolName, timestamp = Date.now()) {
        const history = getHistory();

        // Create history item
        const item = {
            fileName: fileName,
            toolName: toolName,
            timestamp: timestamp,
            date: new Date(timestamp).toLocaleString()
        };

        // Remove duplicate if exists
        const filtered = history.filter(h => !(h.fileName === fileName && h.toolName === toolName));

        // Add to beginning and limit to MAX_HISTORY
        filtered.unshift(item);
        const newHistory = filtered.slice(0, MAX_HISTORY);

        // Save to localStorage
        try {
            localStorage.setItem(HISTORY_KEY, JSON.stringify(newHistory));
            updateHistoryUI();
        } catch (e) {
            console.error('Error saving history:', e);
        }
    }

    // Clear history
    function clearHistory() {
        localStorage.removeItem(HISTORY_KEY);
        updateHistoryUI();
    }

    // Update history UI
    function updateHistoryUI() {
        const historyContainer = document.getElementById('fileHistory');
        if (!historyContainer) return;

        const history = getHistory();

        if (history.length === 0) {
            historyContainer.innerHTML = '<div class="history-empty">No recent files</div>';
            return;
        }

        let html = '';
        history.forEach((item, index) => {
            const timeAgo = getTimeAgo(item.timestamp);
            html += `
                <div class="history-item" data-index="${index}">
                    <div class="history-icon">${getToolIcon(item.toolName)}</div>
                    <div class="history-info">
                        <div class="history-filename" title="${item.fileName}">${truncateFileName(item.fileName, 30)}</div>
                        <div class="history-meta">${item.toolName} • ${timeAgo}</div>
                    </div>
                </div>
            `;
        });

        // Add clear button
        if (history.length > 0) {
            html += '<button class="history-clear-btn" onclick="window.clearFileHistory()">Clear History</button>';
        }

        historyContainer.innerHTML = html;
    }

    // Get tool icon based on tool name
    function getToolIcon(toolName) {
        const icons = {
            'PDF': '📄',
            'Image': '🖼️',
            'QR': '📱',
            'Word': '📝',
            'Excel': '📊',
            'PowerPoint': '📽️',
            'Compress': '🗜️',
            'Resize': '📏',
            'Convert': '🔄',
            'Default': '📁'
        };

        for (const key in icons) {
            if (toolName.includes(key)) {
                return icons[key];
            }
        }
        return icons.Default;
    }

    // Truncate long file names
    function truncateFileName(name, maxLength) {
        if (name.length <= maxLength) return name;

        const ext = name.split('.').pop();
        const baseName = name.substring(0, name.length - ext.length - 1);
        const truncated = baseName.substring(0, maxLength - ext.length - 4) + '...';

        return truncated + '.' + ext;
    }

    // Get relative time
    function getTimeAgo(timestamp) {
        const seconds = Math.floor((Date.now() - timestamp) / 1000);

        if (seconds < 60) return 'Just now';
        if (seconds < 3600) return Math.floor(seconds / 60) + 'm ago';
        if (seconds < 86400) return Math.floor(seconds / 3600) + 'h ago';
        if (seconds < 604800) return Math.floor(seconds / 86400) + 'd ago';

        return new Date(timestamp).toLocaleDateString();
    }

    // Initialize on page load
    document.addEventListener('DOMContentLoaded', function() {
        updateHistoryUI();

        // Auto-track file inputs
        const fileInputs = document.querySelectorAll('input[type="file"]');
        fileInputs.forEach(input => {
            input.addEventListener('change', function(e) {
                if (this.files && this.files[0]) {
                    const fileName = this.files[0].name;
                    const toolName = document.title.split('-')[0].trim() || 'Tool';

                    // Add to history after a short delay (to confirm user action)
                    setTimeout(() => {
                        addToHistory(fileName, toolName);
                    }, 500);
                }
            });
        });
    });

    // Expose functions globally
    window.addToFileHistory = addToHistory;
    window.clearFileHistory = clearHistory;
    window.updateFileHistory = updateHistoryUI;
})();
