// Dark Mode Toggle (Optional)
// Since TTS tool uses dark theme by default, this is minimal

(function() {
    // Check for saved theme preference or default to dark
    const currentTheme = localStorage.getItem('theme') || 'dark';

    if (currentTheme === 'dark') {
        document.body.classList.add('dark-mode');
    }
})();
