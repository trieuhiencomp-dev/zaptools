#!/usr/bin/env python3
"""
Script to add file history and dark mode to all tool pages
"""

import os
import glob

# Get all tool HTML files (except Index.html and blog pages)
tool_pages = glob.glob('Y:/zaptools/*.html')
exclude = ['Index.html', 'blog.html', 'privacy-policy.html', 'pdf-tools.html', 'image-tool.html', 'QRcode.html']
tool_pages = [f for f in tool_pages if os.path.basename(f) not in exclude]

print(f"Found {len(tool_pages)} tool pages to update\n")

# Widget HTML
widget_html = '''
<!-- File History Widget -->
<div class="file-history-widget collapsed" id="historyWidget">
    <div class="history-header" onclick="document.getElementById('historyWidget').classList.toggle('collapsed')">
        <div class="history-title">
            <span>📋</span>
            <span>Recent Files</span>
        </div>
        <div class="history-toggle">▼</div>
    </div>
    <div class="history-content" id="fileHistory">
        <div class="history-empty">No recent files</div>
    </div>
</div>

<!-- Dark Mode Toggle -->
<button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode">
    <span id="themeIcon">🌙</span>
    <span class="theme-toggle-text" id="themeText">Dark</span>
</button>

'''

updated_count = 0

for page_path in tool_pages:
    try:
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()

        modified = False

        # 1. Add CSS links before </head>
        if 'file-history.css' not in content and '</head>' in content:
            content = content.replace(
                '</head>',
                '    <link rel="stylesheet" href="file-history.css">\n    <link rel="stylesheet" href="dark-mode.css">\n</head>'
            )
            modified = True

        # 2. Add widget before </body>
        if 'file-history-widget' not in content and '</body>' in content:
            content = content.replace('</body>', widget_html + '</body>')
            modified = True

        # 3. Add JS scripts before </body>
        if 'file-history.js' not in content and '</body>' in content:
            content = content.replace(
                '</body>',
                '    <script src="file-history.js"></script>\n    <script src="dark-mode.js"></script>\n</body>'
            )
            modified = True

        if modified:
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"[OK] Updated: {os.path.basename(page_path)}")
        else:
            print(f"[SKIP] Already has features: {os.path.basename(page_path)}")

    except Exception as e:
        print(f"[ERROR] Failed to update {os.path.basename(page_path)}: {e}")

print(f"\n[SUCCESS] Updated {updated_count}/{len(tool_pages)} pages")
print("\nAdded features:")
print("  * File history widget (bottom-right)")
print("  * Dark mode toggle (top-right)")
print("  * Auto-track uploaded files")
print("  * System theme preference detection")
