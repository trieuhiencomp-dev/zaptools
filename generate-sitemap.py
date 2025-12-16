import os
from datetime import datetime

# Get all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Base URL
base_url = 'https://zaptools.org'

# Current date in ISO format
current_date = datetime.now().strftime('%Y-%m-%d')

# Start sitemap XML
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

# Priority mapping
priority_map = {
    'Index.html': ('1.0', 'daily'),
    'index.html': ('1.0', 'daily'),
    'blog.html': ('0.9', 'weekly'),
    'feedback.html': ('0.7', 'monthly'),
    'privacy-policy.html': ('0.5', 'monthly'),
}

# Add each HTML file to sitemap
for html_file in sorted(html_files):
    # Determine priority and change frequency
    if html_file in priority_map:
        priority, changefreq = priority_map[html_file]
    else:
        priority = '0.8'
        changefreq = 'weekly'

    # Create URL entry
    if html_file == 'Index.html':
        url = f'{base_url}/'
    else:
        url = f'{base_url}/{html_file}'

    sitemap += '  <url>\n'
    sitemap += f'    <loc>{url}</loc>\n'
    sitemap += f'    <lastmod>{current_date}</lastmod>\n'
    sitemap += f'    <changefreq>{changefreq}</changefreq>\n'
    sitemap += f'    <priority>{priority}</priority>\n'
    sitemap += '  </url>\n'

# Close sitemap XML
sitemap += '</urlset>'

# Write sitemap to file
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)

print(f'[OK] Da tao sitemap.xml voi {len(html_files)} trang')
print(f'     Base URL: {base_url}')
print(f'     Last modified: {current_date}')
