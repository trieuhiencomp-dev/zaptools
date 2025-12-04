#!/usr/bin/env python3
"""
Update OG image paths in HTML files
"""
import os
import re
import glob

def update_og_paths(file_path):
    """Update OG image paths in HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Fix specific wrong references first
        content = content.replace(
            'og-image-image-compression.png',
            'og-images/og-image-image-compression-tips.png'
        )
        content = content.replace(
            'og-image-qr-business.png',
            'og-images/og-image-qr-codes-for-business.png'
        )

        # Update all og:image paths to use og-images/ folder
        # Match: content="https://zaptools.org/og-image-XXX.png"
        # Replace with: content="https://zaptools.org/og-images/og-image-XXX.png"
        pattern = r'property="og:image"\s+content="https://zaptools\.org/og-image-'
        replacement = r'property="og:image" content="https://zaptools.org/og-images/og-image-'
        content = re.sub(pattern, replacement, content)

        # Also handle twitter:image
        pattern = r'name="twitter:image"\s+content="https://zaptools\.org/og-image-'
        replacement = r'name="twitter:image" content="https://zaptools.org/og-images/og-image-'
        content = re.sub(pattern, replacement, content)

        # Only write if changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"[ERROR] {file_path}: {str(e)}")
        return False

def main():
    """Update all HTML files"""
    print("Updating OG image paths in HTML files...\n")

    # Get all HTML files
    html_files = []
    html_files.extend(glob.glob("*.html"))
    html_files.extend(glob.glob("blog/*.html"))

    updated_count = 0

    for html_file in html_files:
        if update_og_paths(html_file):
            print(f"[OK] Updated: {html_file}")
            updated_count += 1
        else:
            print(f"[SKIP] No changes: {html_file}")

    print(f"\n[SUCCESS] Updated {updated_count} files!")
    print("[SUCCESS] All OG image paths now point to og-images/ folder")

if __name__ == '__main__':
    main()
