#!/usr/bin/env python3
"""
Script to replace AdSense placeholder with real code
"""

import os
import glob

# Real AdSense code
REAL_ADSENSE_CODE = '''
    <!-- Google AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6389544196145251"
     crossorigin="anonymous"></script>
'''

def replace_adsense_placeholder(file_path):
    """Replace placeholder AdSense code with real code"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has real AdSense code
    if 'ca-pub-6389544196145251' in content:
        print(f"[OK] {os.path.basename(file_path)} already has real AdSense code")
        return False

    # Check if has placeholder
    if 'ca-pub-XXXXXXXXXX' not in content and 'Google AdSense' not in content:
        print(f"[SKIP] {os.path.basename(file_path)} doesn't have AdSense placeholder")
        return False

    # Replace the entire commented section with active code
    if '<!-- Google AdSense - REPLACE WITH YOUR CODE AFTER APPROVAL -->' in content:
        # Find and replace the entire comment block
        old_block = '''    <!-- Google AdSense - REPLACE WITH YOUR CODE AFTER APPROVAL -->
    <!-- Uncomment after getting approved:
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXX" crossorigin="anonymous"></script>
    -->'''

        content = content.replace(old_block, REAL_ADSENSE_CODE)

    # Also try to replace if it's slightly different format
    elif 'ca-pub-XXXXXXXXXX' in content:
        content = content.replace('ca-pub-XXXXXXXXXX', 'ca-pub-6389544196145251')
        # Remove comment markers
        content = content.replace('<!-- Uncomment after getting approved:', '')
        content = content.replace('-->', '')

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"[UPDATED] {os.path.basename(file_path)}")
    return True

def main():
    # Get all HTML files in current directory
    html_files = glob.glob('*.html')

    print(f"Found {len(html_files)} HTML files\n")
    print("Replacing placeholder with real AdSense code...")
    print("Publisher ID: ca-pub-6389544196145251\n")

    updated_count = 0
    for file_path in sorted(html_files):
        if replace_adsense_placeholder(file_path):
            updated_count += 1

    print(f"\n[DONE] Updated {updated_count} files with real AdSense code")
    print(f"[INFO] {len(html_files) - updated_count} files already had it or no placeholder")

if __name__ == '__main__':
    main()
