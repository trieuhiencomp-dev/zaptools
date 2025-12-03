#!/usr/bin/env python3
"""
Script to add feedback widget to all HTML files
"""

import os
import glob

# The script tag to add
FEEDBACK_WIDGET = '''
    <!-- Feedback Widget -->
    <script src="feedback-widget.js"></script>'''

def add_feedback_widget(file_path):
    """Add feedback widget script before </body> tag if not already present"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has feedback widget
    if 'feedback-widget.js' in content:
        print(f"[OK] {os.path.basename(file_path)} already has feedback widget")
        return False

    # Check if has </body> tag
    if '</body>' not in content:
        print(f"[SKIP] {os.path.basename(file_path)} doesn't have </body> tag")
        return False

    # Add feedback widget before </body>
    content = content.replace('</body>', f'{FEEDBACK_WIDGET}\n</body>')

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"[ADDED] {os.path.basename(file_path)}")
    return True

def main():
    # Get all HTML files in current directory
    html_files = glob.glob('*.html')

    print(f"Found {len(html_files)} HTML files\n")

    added_count = 0
    for file_path in sorted(html_files):
        if add_feedback_widget(file_path):
            added_count += 1

    print(f"\n[DONE] Added feedback widget to {added_count} files")
    print(f"[INFO] {len(html_files) - added_count} files already had it or no </body> tag")

if __name__ == '__main__':
    main()
