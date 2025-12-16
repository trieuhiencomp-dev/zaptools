#!/usr/bin/env python3
"""
Script to optimize meta tags for all PDF tool pages to improve CTR
"""

import re

# Optimized meta tags for each PDF tool page
pdf_pages_meta = {
    'PDFtoPowerpoint.html': {
        'title': 'PDF to PowerPoint Converter Free 2025 - Convert PDF to PPTX Online | ZapTools',
        'description': 'Convert PDF to PowerPoint presentations instantly! Free, fast, and secure. No signup required. Transform PDF documents into editable PPTX slides in seconds. 100% free online PDF to PowerPoint converter.',
        'keywords': 'pdf to powerpoint, pdf to pptx, convert pdf to presentation, pdf to powerpoint free, pdf to ppt online, pdf converter, free pdf to powerpoint converter 2025'
    },
    'PDFtoImage.html': {
        'title': 'PDF to Image Converter Free 2025 - Convert PDF to JPG/PNG Online | ZapTools',
        'description': 'Convert PDF to JPG or PNG images for free! High-quality PDF to image conversion. No watermark, no signup. Extract all pages or select specific ones. Fast, secure, and 100% free PDF to image converter online.',
        'keywords': 'pdf to image, pdf to jpg, pdf to png, convert pdf to image, pdf to jpeg, free pdf to image converter, pdf image converter online 2025'
    },
    'PDFresize.html': {
        'title': 'PDF Resizer Free 2025 - Resize & Reduce PDF File Size Online | ZapTools',
        'description': 'Resize PDF files and reduce PDF file size online for free! Compress PDF without losing quality. Change PDF dimensions, scale pages, optimize file size. No watermark, no signup. Free online PDF resizer tool 2025.',
        'keywords': 'resize pdf, pdf resizer, reduce pdf size, compress pdf, change pdf size, pdf file size reducer, resize pdf online free, pdf resizer tool 2025'
    },
    'PDFtoWord.html': {
        'title': 'PDF to Word Converter Free 2025 - Convert PDF to DOCX Online | ZapTools',
        'description': 'Convert PDF to Word (DOCX) documents for free! Editable, accurate conversion. No signup, no watermark. Transform PDF files into Microsoft Word format instantly. 100% free PDF to Word converter online.',
        'keywords': 'pdf to word, pdf to docx, convert pdf to word, pdf to doc, free pdf to word converter, pdf word converter online 2025'
    },
    'PDFtoExcel.html': {
        'title': 'PDF to Excel Converter Free 2025 - Convert PDF to XLSX Online | ZapTools',
        'description': 'Convert PDF to Excel spreadsheets for free! Extract tables from PDF to XLSX. No signup required. Accurate data conversion, editable Excel files. Free online PDF to Excel converter 2025.',
        'keywords': 'pdf to excel, pdf to xlsx, convert pdf to excel, pdf to spreadsheet, free pdf to excel converter, pdf excel converter online 2025'
    },
    'MergePDFs.html': {
        'title': 'Merge PDF Files Free 2025 - Combine Multiple PDFs Online | ZapTools',
        'description': 'Merge multiple PDF files into one for free! Combine, join, and concatenate PDFs online. No file limits, no watermark. Fast, secure PDF merger. 100% free online PDF merge tool 2025.',
        'keywords': 'merge pdf, combine pdf, join pdf, pdf merger, merge multiple pdfs, combine pdf files free, pdf merge tool online 2025'
    },
    'SplitPDF.html': {
        'title': 'Split PDF Free 2025 - Extract Pages & Divide PDF Online | ZapTools',
        'description': 'Split PDF files for free! Extract specific pages, divide PDF into multiple files. No watermark, no signup. Fast and secure PDF splitter. 100% free online PDF split tool 2025.',
        'keywords': 'split pdf, divide pdf, extract pdf pages, pdf splitter, split pdf online free, pdf split tool 2025'
    },
    'pdf-tools.html': {
        'title': 'Free PDF Tools Online 2025 - Convert, Merge, Split, Compress PDF | ZapTools',
        'description': 'All-in-one PDF tools online for free! Convert, merge, split, compress, resize PDFs. PDF to Word, Excel, PowerPoint, Image. No signup, no watermark. Your complete PDF solution 2025.',
        'keywords': 'pdf tools, free pdf tools, pdf converter, pdf editor online, merge pdf, split pdf, compress pdf, pdf utilities 2025'
    }
}

def update_meta_tags(filename, new_meta):
    """Update meta tags in a PDF tool page"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update title
        content = re.sub(
            r'<title>.*?</title>',
            f'<title>{new_meta["title"]}</title>',
            content,
            flags=re.DOTALL
        )

        # Update meta description
        content = re.sub(
            r'<meta name="description" content=".*?">',
            f'<meta name="description" content="{new_meta["description"]}">',
            content
        )

        # Update meta keywords
        content = re.sub(
            r'<meta name="keywords" content=".*?">',
            f'<meta name="keywords" content="{new_meta["keywords"]}">',
            content
        )

        # Update OG title
        content = re.sub(
            r'<meta property="og:title" content=".*?">',
            f'<meta property="og:title" content="{new_meta["title"]}">',
            content
        )

        # Update OG description
        content = re.sub(
            r'<meta property="og:description" content=".*?">',
            f'<meta property="og:description" content="{new_meta["description"][:160]}">',
            content
        )

        # Update Twitter title
        content = re.sub(
            r'<meta name="twitter:title" content=".*?">',
            f'<meta name="twitter:title" content="{new_meta["title"]}">',
            content
        )

        # Update Twitter description
        content = re.sub(
            r'<meta name="twitter:description" content=".*?">',
            f'<meta name="twitter:description" content="{new_meta["description"][:160]}">',
            content
        )

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[OK] Optimized meta tags for {filename}")
        return True

    except Exception as e:
        print(f"[ERROR] Failed to update {filename}: {e}")
        return False

def main():
    import os
    os.chdir('Y:/zaptools')

    updated_count = 0
    for filename, meta in pdf_pages_meta.items():
        if os.path.exists(filename):
            if update_meta_tags(filename, meta):
                updated_count += 1
        else:
            print(f"[SKIP] {filename} not found")

    print(f"\n[SUCCESS] Optimized meta tags for {updated_count}/{len(pdf_pages_meta)} PDF pages!")
    print("New meta tags are designed to improve CTR with:")
    print("  - Year (2025) for freshness")
    print("  - Key benefits (free, no signup, no watermark)")
    print("  - Action-oriented language")
    print("  - Exact keyword matches from search queries")

if __name__ == "__main__":
    main()
