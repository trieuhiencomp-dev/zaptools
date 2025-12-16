import os
import re

# CSS for ads
ad_css = """
        /* Ad Styles */
        .ad-container {
            max-width: 1200px;
            margin: 1rem auto;
            padding: 0.5rem;
            text-align: center;
        }
        .ad-label {
            font-size: 0.7rem;
            color: rgba(255,255,255,0.5);
            margin-bottom: 0.3rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .top-ad {
            margin-bottom: 1.5rem;
        }
        .bottom-ad {
            margin-top: 1.5rem;
        }
        @media (max-width: 768px) {
            .ad-container {
                padding: 0.3rem;
            }
        }
"""

# Top Ad HTML
top_ad = """    <!-- Top Ad -->
    <div class="top-ad ad-container">
        <div class="ad-label">Advertisement</div>
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="ca-pub-6389544196145251"
             data-ad-slot="3131107512"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>
             (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
    </div>

"""

# Bottom Ad HTML
bottom_ad = """
    <!-- Bottom Ad -->
    <div class="bottom-ad ad-container">
        <div class="ad-label">Advertisement</div>
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="ca-pub-6389544196145251"
             data-ad-slot="3131107512"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>
             (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
    </div>
"""

html_files = [
    'barcode-generator.html', 'base64-encoder.html', 'blog.html', 'calculator.html',
    'case-converter.html', 'code-beautifier.html', 'code-minifier.html',
    'color-palette-extractor.html', 'color-picker.html', 'csv-to-json.html',
    'DanhSachTaoQR.html', 'diff-checker.html', 'email-validator.html', 'feedback.html',
    'file-history-widget.html', 'GiaiMaQR.html', 'hash-generator.html', 'html-encoder.html',
    'ImageCompress.html', 'ImageConvert.html', 'image-cropper.html', 'ImageResize.html',
    'image-tool.html', 'image-to-text.html', 'ip-lookup.html',
    'json-formatter.html', 'json-to-xml.html', 'jwt-decoder.html', 'lorem-ipsum.html',
    'markdown-editor.html', 'meme-generator.html', 'MergePDFs.html', 'meta-tag-generator.html',
    'password-generator.html', 'PDFresize.html', 'PDFtoExcel.html', 'PDFtoImage.html',
    'pdf-tools.html', 'PDFtoPowerpoint.html', 'PDFtoWord.html', 'privacy-policy.html',
    'QRcode.html', 'QRcontact.html', 'QRevent.html', 'QRlinkweb.html', 'QRproduct.html',
    'QRwifi.html', 'random-name-generator.html', 'regex-tester.html', 'screenshot-tool.html',
    'social-proof-elements.html', 'SplitPDF.html', 'sql-formatter.html', 'stopwatch.html',
    'text-to-video.html', 'timestamp-converter.html', 'tts-tool.html', 'tts-tool-local.html',
    'unit-converter.html', 'url-encoder.html', 'url-shortener.html', 'uuid-generator.html',
    'word-counter.html', 'youtube-thumbnail-downloader.html', 'gradient-generator.html'
]

processed = 0
skipped = 0
errors = 0

for filename in html_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if ads already exist
        if 'ad-container' in content and 'Top Ad' in content:
            print(f'[SKIP] {filename} - da co quang cao')
            skipped += 1
            continue

        # 1. Add CSS for ads before </style>
        if '</style>' in content:
            content = content.replace('</style>', ad_css + '    </style>', 1)
        else:
            print(f'[WARNING] Khong tim thay </style> trong {filename}')

        # 2. Add top ad after <body> or after opening body tag
        # Find the first substantial content after <body>
        body_match = re.search(r'<body[^>]*>\s*', content)
        if body_match:
            insert_pos = body_match.end()
            content = content[:insert_pos] + top_ad + content[insert_pos:]
        else:
            print(f'[WARNING] Khong tim thay <body> trong {filename}')

        # 3. Add bottom ad before </body>
        if '</body>' in content:
            content = content.replace('</body>', bottom_ad + '</body>', 1)
        else:
            print(f'[WARNING] Khong tim thay </body> trong {filename}')

        # Write the updated content
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f'[OK] Da them quang cao vao {filename}')
        processed += 1

    except Exception as e:
        print(f'[ERROR] Loi khi xu ly {filename}: {str(e)}')
        errors += 1

print(f'\nTONG KET:')
print(f'   Da xu ly: {processed} file')
print(f'   Da bo qua: {skipped} file')
print(f'   Loi: {errors} file')
