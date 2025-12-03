#!/usr/bin/env python3
"""
Script to add Google AdSense placeholder to all HTML files
"""

import os
import glob
import re

# The AdSense placeholder to add
ADSENSE_PLACEHOLDER = '''
    <!-- Google AdSense - REPLACE WITH YOUR CODE AFTER APPROVAL -->
    <!-- Uncomment after getting approved:
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXX" crossorigin="anonymous"></script>
    -->
'''

def add_adsense_placeholder(file_path):
    """Add AdSense placeholder in <head> section if not already present"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has AdSense
    if 'adsbygoogle' in content or 'Google AdSense' in content:
        print(f"[OK] {os.path.basename(file_path)} already has AdSense")
        return False

    # Check if has <head> tag
    if '<head>' not in content:
        print(f"[SKIP] {os.path.basename(file_path)} doesn't have <head> tag")
        return False

    # Find the position after meta tags but before <style> or </head>
    # Try to insert after last <meta> tag or <title>

    # Pattern 1: After meta description
    if '<meta name="description"' in content:
        content = re.sub(
            r'(<meta name="description"[^>]*>)',
            r'\1' + ADSENSE_PLACEHOLDER,
            content,
            count=1
        )
    # Pattern 2: After title tag
    elif '</title>' in content:
        content = content.replace('</title>', '</title>' + ADSENSE_PLACEHOLDER, 1)
    # Pattern 3: After <head> tag
    else:
        content = content.replace('<head>', '<head>' + ADSENSE_PLACEHOLDER, 1)

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
        if add_adsense_placeholder(file_path):
            added_count += 1

    print(f"\n[DONE] Added AdSense placeholder to {added_count} files")
    print(f"[INFO] {len(html_files) - added_count} files already had it or no <head> tag")

if __name__ == '__main__':
    main()
