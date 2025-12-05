// Social Proof & Stats Counter
(function() {
    'use strict';

    // Animated counter
    function animateCounter(element, target, duration = 2000) {
        const start = 0;
        const increment = target / (duration / 16);
        let current = start;

        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                element.textContent = Math.floor(target).toLocaleString();
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(current).toLocaleString();
            }
        }, 16);
    }

    // Initialize stats
    function initStats() {
        const statsContainer = document.querySelector('.stats-container');
        if (!statsContainer) return;

        // Get base numbers from localStorage or generate random
        let toolsUsed = parseInt(localStorage.getItem('zaptools_total_conversions') || Math.floor(Math.random() * 5000 + 15000));
        let usersToday = Math.floor(Math.random() * 200 + 800);
        let happyUsers = Math.floor(toolsUsed * 0.85);

        // Update localStorage
        localStorage.setItem('zaptools_total_conversions', toolsUsed);

        // Animate counters
        const counters = statsContainer.querySelectorAll('.stat-number');
        if (counters[0]) animateCounter(counters[0], toolsUsed, 2000);
        if (counters[1]) animateCounter(counters[1], usersToday, 1500);
        if (counters[2]) animateCounter(counters[2], happyUsers, 2200);

        // Increment total conversions periodically
        setInterval(() => {
            toolsUsed += Math.floor(Math.random() * 3 + 1);
            localStorage.setItem('zaptools_total_conversions', toolsUsed);
            if (counters[0]) counters[0].textContent = toolsUsed.toLocaleString();
        }, 15000);
    }

    // Activity feed simulation
    const activities = [
        { en: 'Someone compressed a PDF', vi: 'Ai đó đã nén một file PDF' },
        { en: 'User converted image to WebP', vi: 'Người dùng chuyển ảnh sang WebP' },
        { en: 'PDF converted to Word', vi: 'PDF được chuyển sang Word' },
        { en: 'QR code generated', vi: 'Mã QR được tạo' },
        { en: 'Image resized successfully', vi: 'Ảnh được thay đổi kích thước' },
        { en: 'Password generated', vi: 'Mật khẩu được tạo' },
        { en: 'JSON formatted', vi: 'JSON được định dạng' },
        { en: 'Hash generated', vi: 'Hash được tạo' }
    ];

    function addActivity() {
        const feed = document.getElementById('activityFeed');
        if (!feed) return;

        const lang = localStorage.getItem('zaptools_lang') || 'vi';
        const randomActivity = activities[Math.floor(Math.random() * activities.length)];
        const timeAgo = Math.floor(Math.random() * 5 + 1);

        const item = document.createElement('div');
        item.className = 'activity-item';
        item.textContent = randomActivity[lang] + ' • ' + timeAgo + (lang === 'vi' ? ' phút trước' : ' min ago');

        feed.insertBefore(item, feed.firstChild);

        // Keep only last 3 items
        while (feed.children.length > 3) {
            feed.removeChild(feed.lastChild);
        }
    }

    // Initialize on page load
    document.addEventListener('DOMContentLoaded', function() {
        initStats();

        // Add initial activities
        setTimeout(() => addActivity(), 1000);
        setTimeout(() => addActivity(), 2000);
        setTimeout(() => addActivity(), 3000);

        // Add new activity every 8-12 seconds
        setInterval(() => {
            addActivity();
        }, Math.random() * 4000 + 8000);
    });
})();
