#!/usr/bin/env python3
"""
Submit URLs to Google Search Console via Indexing API
Requires: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
"""

import json
import time
from datetime import datetime

def read_urls():
    """Read URLs from sitemap.xml"""
    urls = []
    try:
        with open('sitemap.xml', 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract URLs
            import re
            urls = re.findall(r'<loc>(.*?)</loc>', content)
    except Exception as e:
        print(f"Error reading sitemap: {e}")

    return urls

def create_index_request_batch():
    """Create batch request for Google Indexing API"""
    urls = read_urls()

    print(f"Found {len(urls)} URLs to submit")

    # Create batch request format for Google Search Console
    batch_data = {
        "urls": urls,
        "timestamp": datetime.now().isoformat(),
        "total": len(urls)
    }

    # Save to file for manual submission
    with open('google-index-batch.json', 'w', encoding='utf-8') as f:
        json.dump(batch_data, f, indent=2)

    print(f"\nCreated google-index-batch.json with {len(urls)} URLs")
    print("\nIMPORTANT: Google Indexing API requires authentication.")
    print("Please follow these steps:")
    print("\n1. Go to Google Search Console: https://search.google.com/search-console")
    print("2. Select your property: zaptools.org")
    print("3. Go to 'Sitemaps' and submit: sitemap.xml")
    print("4. Use 'URL Inspection' tool to request indexing for priority pages")
    print("\nPriority pages to submit manually:")
    priority_urls = [
        "https://zaptools.org/",
        "https://zaptools.org/PDFtoExcel.html",
        "https://zaptools.org/SplitPDF.html",
        "https://zaptools.org/blog-kinh-nghiem-hay.html",
    ]

    for url in priority_urls:
        print(f"  - {url}")

    print("\n\nAlternatively, use Google's bulk submission:")
    print("https://search.google.com/search-console/index")

if __name__ == '__main__':
    create_index_request_batch()
