#!/usr/bin/env python3
"""
Script to automatically add comprehensive SEO meta tags to all HTML files
"""

import os
import re
from pathlib import Path

# SEO configuration for different page types
SEO_CONFIG = {
    'image-tool.html': {
        'title': 'Free Image Tools - Compress, Resize, Convert | ZapTools',
        'description': 'Free online image tools. Compress images, resize photos, convert image formats (JPG, PNG, WebP). Fast, secure, no signup required!',
        'keywords': 'image compressor, resize image, convert image, image tools, compress jpg, png to jpg, webp converter',
        'type': 'WebApplication',
        'features': ['Image Compression', 'Image Resize', 'Image Format Conversion']
    },
    'pdf-tools.html': {
        'title': 'Free PDF Tools - Convert, Merge, Split PDF | ZapTools',
        'description': 'Free online PDF tools. Convert PDF to Word/Excel/Image, merge PDFs, split PDF files. 100% free, secure, no watermarks!',
        'keywords': 'pdf converter, pdf to word, pdf to excel, merge pdf, split pdf, pdf tools',
        'type': 'WebApplication',
        'features': ['PDF to Word', 'PDF to Excel', 'PDF Merge', 'PDF Split', 'PDF to Image']
    },
    'QRcode.html': {
        'title': 'Free QR Code Generator - Create QR Codes Online | ZapTools',
        'description': 'Create QR codes for free. Generate QR codes for URLs, WiFi, contact info, events, products. No limits, high quality!',
        'keywords': 'qr code generator, create qr code, qr code maker, wifi qr code, vcard qr code',
        'type': 'WebApplication',
        'features': ['URL QR Code', 'WiFi QR Code', 'Contact QR Code', 'Event QR Code']
    },
    'ImageCompress.html': {
        'title': 'Free Image Compressor - Compress JPG, PNG Online | ZapTools',
        'description': 'Compress images online for free. Reduce JPG, PNG, WebP file size without quality loss. Fast compression, secure!',
        'keywords': 'image compressor, compress jpg, compress png, reduce image size, optimize images',
        'type': 'WebApplication',
        'features': ['JPG Compression', 'PNG Compression', 'WebP Compression', 'Batch Compression']
    },
    'ImageResize.html': {
        'title': 'Free Image Resizer - Resize Photos Online | ZapTools',
        'description': 'Resize images online for free. Change image dimensions, scale photos, resize for social media. Fast and easy!',
        'keywords': 'image resizer, resize photo, scale image, change image size, photo dimensions',
        'type': 'WebApplication',
        'features': ['Image Resize', 'Photo Scaling', 'Dimension Change', 'Aspect Ratio Lock']
    },
    'ImageConvert.html': {
        'title': 'Free Image Converter - Convert JPG, PNG, WebP | ZapTools',
        'description': 'Convert image formats online for free. JPG to PNG, PNG to WebP, and more. Fast conversion, no quality loss!',
        'keywords': 'image converter, jpg to png, png to jpg, webp converter, convert image format',
        'type': 'WebApplication',
        'features': ['JPG to PNG', 'PNG to JPG', 'WebP Conversion', 'Format Conversion']
    },
    'PDFtoWord.html': {
        'title': 'Free PDF to Word Converter Online | ZapTools',
        'description': 'Convert PDF to Word (DOCX) online for free. Accurate conversion, preserves formatting. No limits!',
        'keywords': 'pdf to word, pdf to docx, convert pdf to word, pdf converter',
        'type': 'WebApplication',
        'features': ['PDF to Word', 'PDF to DOCX', 'Format Preservation']
    },
    'PDFtoExcel.html': {
        'title': 'Free PDF to Excel Converter Online | ZapTools',
        'description': 'Convert PDF to Excel (XLSX) online for free. Extract tables from PDF, convert to spreadsheet!',
        'keywords': 'pdf to excel, pdf to xlsx, convert pdf to excel, extract pdf tables',
        'type': 'WebApplication',
        'features': ['PDF to Excel', 'PDF to XLSX', 'Table Extraction']
    },
    'PDFtoImage.html': {
        'title': 'Free PDF to Image Converter - PDF to JPG/PNG | ZapTools',
        'description': 'Convert PDF to images online for free. PDF to JPG, PDF to PNG. High quality conversion!',
        'keywords': 'pdf to image, pdf to jpg, pdf to png, convert pdf to image',
        'type': 'WebApplication',
        'features': ['PDF to JPG', 'PDF to PNG', 'High Quality Output']
    },
    'PDFtoPowerpoint.html': {
        'title': 'Free PDF to PowerPoint Converter Online | ZapTools',
        'description': 'Convert PDF to PowerPoint (PPTX) online for free. Transform PDFs into editable presentations!',
        'keywords': 'pdf to powerpoint, pdf to pptx, convert pdf to presentation',
        'type': 'WebApplication',
        'features': ['PDF to PowerPoint', 'PDF to PPTX', 'Editable Output']
    },
    'MergePDFs.html': {
        'title': 'Free PDF Merger - Combine Multiple PDFs Online | ZapTools',
        'description': 'Merge PDF files online for free. Combine multiple PDFs into one document. Fast, secure, no limits!',
        'keywords': 'merge pdf, combine pdf, pdf merger, join pdf files',
        'type': 'WebApplication',
        'features': ['Merge Multiple PDFs', 'Combine Documents', 'Drag & Drop']
    },
    'SplitPDF.html': {
        'title': 'Free PDF Splitter - Split PDF Pages Online | ZapTools',
        'description': 'Split PDF files online for free. Extract pages, divide PDF into multiple files. Easy and fast!',
        'keywords': 'split pdf, divide pdf, extract pdf pages, pdf splitter',
        'type': 'WebApplication',
        'features': ['Split PDF', 'Extract Pages', 'Multiple Output Files']
    },
    'PDFresize.html': {
        'title': 'Free PDF Resizer - Resize PDF Pages Online | ZapTools',
        'description': 'Resize PDF pages online for free. Change PDF dimensions, scale PDF content. No quality loss!',
        'keywords': 'resize pdf, pdf resizer, scale pdf, change pdf size',
        'type': 'WebApplication',
        'features': ['Resize PDF Pages', 'Scale Content', 'Custom Dimensions']
    },
    'DanhSachTaoQR.html': {
        'title': 'QR Code Types - Choose Your QR Code Format | ZapTools',
        'description': 'Create different types of QR codes. URL, WiFi, Contact, Event, Product QR codes. Free and unlimited!',
        'keywords': 'qr code types, qr code formats, generate qr code',
        'type': 'WebApplication',
        'features': ['Multiple QR Types', 'Custom QR Codes', 'Free Generation']
    },
    'QRlinkweb.html': {
        'title': 'Free URL QR Code Generator | ZapTools',
        'description': 'Generate URL QR codes for free. Create QR codes for websites, links. Instant generation!',
        'keywords': 'url qr code, link qr code, website qr code generator',
        'type': 'WebApplication',
        'features': ['URL QR Code', 'Link QR Generation', 'Instant Preview']
    },
    'QRwifi.html': {
        'title': 'Free WiFi QR Code Generator | ZapTools',
        'description': 'Create WiFi QR codes for free. Share WiFi password easily. Scan to connect!',
        'keywords': 'wifi qr code, wifi password qr, share wifi qr code',
        'type': 'WebApplication',
        'features': ['WiFi QR Code', 'Easy Sharing', 'Secure Connection']
    },
    'QRcontact.html': {
        'title': 'Free Contact QR Code (vCard) Generator | ZapTools',
        'description': 'Create contact QR codes (vCard) for free. Share contact information easily!',
        'keywords': 'vcard qr code, contact qr code, business card qr',
        'type': 'WebApplication',
        'features': ['vCard QR Code', 'Contact Sharing', 'Digital Business Card']
    },
    'QRevent.html': {
        'title': 'Free Event QR Code Generator | ZapTools',
        'description': 'Create event QR codes for free. Generate QR codes for calendar events!',
        'keywords': 'event qr code, calendar qr code, meeting qr code',
        'type': 'WebApplication',
        'features': ['Event QR Code', 'Calendar Integration', 'Quick Add']
    },
    'QRproduct.html': {
        'title': 'Free Product QR Code Generator | ZapTools',
        'description': 'Create product QR codes for free. Link to product information, reviews!',
        'keywords': 'product qr code, item qr code, product information qr',
        'type': 'WebApplication',
        'features': ['Product QR Code', 'Product Info', 'Easy Scanning']
    },
    'GiaiMaQR.html': {
        'title': 'Free QR Code Scanner & Decoder Online | ZapTools',
        'description': 'Scan and decode QR codes online for free. Upload image or use camera. Instant results!',
        'keywords': 'qr code scanner, decode qr code, qr code reader, scan qr code online',
        'type': 'WebApplication',
        'features': ['QR Code Scanning', 'Image Upload', 'Camera Support', 'Instant Decode']
    },
    'privacy-policy.html': {
        'title': 'Privacy Policy | ZapTools',
        'description': 'ZapTools privacy policy. Learn how we protect your data and privacy.',
        'keywords': 'privacy policy, data protection, zaptools privacy',
        'type': 'WebPage',
        'features': []
    }
}

def add_seo_tags(file_path):
    """Add comprehensive SEO tags to an HTML file"""

    filename = os.path.basename(file_path)

    # Skip if already processed or not in config
    if filename not in SEO_CONFIG and filename not in ['Index.html', 'unit-converter.html']:
        print(f"Skipping {filename} (no config)")
        return False

    # Skip already processed files
    if filename in ['Index.html', 'unit-converter.html']:
        print(f"Skipping {filename} (already processed)")
        return False

    config = SEO_CONFIG[filename]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already has SEO tags
        if 'og:title' in content or 'twitter:card' in content:
            print(f"[OK] {filename} already has SEO tags")
            return False

        # Check if file has meta description, if not add it
        if '<meta name="description"' not in content:
            # Add description after title
            content = re.sub(
                r'(<title>.*?</title>)',
                r'\1\n    <meta name="description" content="">',
                content
            )

        # Build SEO tags
        url = f"https://zaptools.org/{filename}"
        og_image = f"https://zaptools.org/og-image-{filename.replace('.html', '')}.png"

        features_json = ',\n        '.join([f'"{f}"' for f in config['features']])

        seo_tags = f'''
    <meta name="keywords" content="{config['keywords']}">
    <meta name="author" content="ZapTools">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{url}">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{config['title']}">
    <meta property="og:description" content="{config['description']}">
    <meta property="og:image" content="{og_image}">
    <meta property="og:site_name" content="ZapTools">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="{url}">
    <meta name="twitter:title" content="{config['title']}">
    <meta name="twitter:description" content="{config['description']}">
    <meta name="twitter:image" content="{og_image}">

    <!-- Theme Color -->
    <meta name="theme-color" content="#667eea">

    <!-- Language Alternates -->
    <link rel="alternate" hreflang="en" href="{url}">
    <link rel="alternate" hreflang="vi" href="{url}">
    <link rel="alternate" hreflang="x-default" href="{url}">'''

        # Add Structured Data if features exist
        if config['features']:
            seo_tags += f'''

    <!-- Structured Data -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "{config['type']}",
      "name": "{config['title'].split('|')[0].strip()}",
      "url": "{url}",
      "description": "{config['description']}",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "Any",
      "offers": {{
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }},
      "featureList": [
        {features_json}
      ]
    }}
    </script>'''

        # Update title and description
        content = re.sub(r'<title>.*?</title>', f'<title>{config["title"]}</title>', content, count=1)
        content = re.sub(r'<meta name="description" content="[^"]*">',
                        f'<meta name="description" content="{config["description"]}">', content, count=1)

        # Insert SEO tags after description
        content = re.sub(
            r'(<meta name="description"[^>]*>)',
            r'\1' + seo_tags,
            content,
            count=1
        )

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[SUCCESS] Added SEO tags to {filename}")
        return True

    except Exception as e:
        print(f"[ERROR] Error processing {filename}: {str(e)}")
        return False

def main():
    """Process all HTML files"""
    base_dir = Path(__file__).parent
    html_files = list(base_dir.glob('*.html'))

    print(f"Found {len(html_files)} HTML files\n")

    processed = 0
    for html_file in html_files:
        if add_seo_tags(html_file):
            processed += 1

    print(f"\nSuccessfully processed {processed} files!")

if __name__ == '__main__':
    main()
