#!/usr/bin/env python3
"""
Script to add Google Analytics to all HTML files
"""

import os
import re
from pathlib import Path

# Google Analytics code
GA_CODE = '''    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-2QEQX2T9JX"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-2QEQX2T9JX');
    </script>
'''

def add_google_analytics(file_path):
    """Add Google Analytics to an HTML file"""

    filename = os.path.basename(file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if GA is already added
        if 'gtag.js' in content or 'G-2QEQX2T9JX' in content:
            print(f"[SKIP] {filename} - GA already exists")
            return False

        # Add GA code right after <head> tag
        if '<head>' in content:
            content = content.replace('<head>', '<head>\n' + GA_CODE, 1)

            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"[SUCCESS] Added GA to {filename}")
            return True
        else:
            print(f"[ERROR] No <head> tag found in {filename}")
            return False

    except Exception as e:
        print(f"[ERROR] {filename}: {str(e)}")
        return False

def main():
    """Process all HTML files"""
    base_dir = Path(__file__).parent

    # Get all HTML files in root
    html_files = list(base_dir.glob('*.html'))

    # Get all HTML files in blog directory
    blog_dir = base_dir / 'blog'
    if blog_dir.exists():
        html_files.extend(list(blog_dir.glob('*.html')))

    print(f"Found {len(html_files)} HTML files\n")

    processed = 0
    for html_file in html_files:
        if add_google_analytics(html_file):
            processed += 1

    print(f"\nSuccessfully added Google Analytics to {processed} files!")
    print(f"\nTracking ID: G-2QEQX2T9JX")

if __name__ == '__main__':
    main()
