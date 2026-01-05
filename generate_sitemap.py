#!/usr/bin/env python3
"""
Generate sitemap.xml for ZapTools website
Scans all HTML files and creates proper Google sitemap format
"""

import os
import glob
from datetime import datetime

# Base URL
BASE_URL = "https://zaptools.org"

# Today's date in ISO format
TODAY = datetime.now().strftime("%Y-%m-%d")

# Priority and changefreq settings
PRIORITY_MAP = {
    'index.html': (1.0, 'daily'),
    'about.html': (0.9, 'monthly'),
    'contact.html': (0.9, 'monthly'),
    'faq.html': (0.9, 'monthly'),
    'blog.html': (0.9, 'weekly'),
    'blog-kinh-nghiem-hay.html': (0.9, 'weekly'),
}

# Default for tool pages
DEFAULT_TOOL = (0.8, 'weekly')
DEFAULT_BLOG_POST = (0.7, 'monthly')

def get_priority_changefreq(filename):
    """Get priority and changefreq for a file"""
    if filename in PRIORITY_MAP:
        return PRIORITY_MAP[filename]
    elif filename.startswith('blog/'):
        return DEFAULT_BLOG_POST
    else:
        return DEFAULT_TOOL

def generate_sitemap():
    """Generate sitemap.xml"""
    # Find all HTML files
    html_files = []

    # Root directory HTML files
    for file in glob.glob('*.html'):
        if file not in ['file-history-widget.html']:  # Exclude utility files
            html_files.append(file)

    # Blog directory HTML files
    if os.path.exists('blog'):
        for file in glob.glob('blog/*.html'):
            html_files.append(file)

    # Sort files
    html_files.sort()

    # Start XML
    xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    # Add homepage first
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{BASE_URL}/</loc>')
    xml_lines.append(f'    <lastmod>{TODAY}</lastmod>')
    xml_lines.append('    <changefreq>daily</changefreq>')
    xml_lines.append('    <priority>1.0</priority>')
    xml_lines.append('  </url>')

    # Add each HTML file
    for file in html_files:
        if file == 'index.html':
            continue  # Already added as homepage

        priority, changefreq = get_priority_changefreq(file)
        url = f'{BASE_URL}/{file}'

        xml_lines.append('  <url>')
        xml_lines.append(f'    <loc>{url}</loc>')
        xml_lines.append(f'    <lastmod>{TODAY}</lastmod>')
        xml_lines.append(f'    <changefreq>{changefreq}</changefreq>')
        xml_lines.append(f'    <priority>{priority}</priority>')
        xml_lines.append('  </url>')

    xml_lines.append('</urlset>')

    # Write to file
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_lines))

    print(f'Generated sitemap.xml with {len(html_files) + 1} URLs')
    print(f'Last modified: {TODAY}')

if __name__ == '__main__':
    generate_sitemap()
