import os
import re

# CSS for sidebar ads (from Index.html)
sidebar_css = """
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
        .page-wrapper {
            display: flex;
            max-width: 1400px;
            margin: 0 auto;
            gap: 1rem;
            align-items: flex-start;
        }
        .sidebar-ad {
            width: 160px;
            position: sticky;
            top: 20px;
        }
        .main-content {
            flex: 1;
        }
        .bottom-ad {
            margin-top: 1.5rem;
        }
        @media (max-width: 1024px) {
            .sidebar-ad {
                display: none;
            }
            .page-wrapper {
                display: block;
            }
        }
"""

# Left Sidebar Ad
left_sidebar = """    <div class="page-wrapper">
        <!-- Left Sidebar Ad -->
        <div class="sidebar-ad">
            <div class="ad-container">
                <div class="ad-label">Ad</div>
                <ins class="adsbygoogle"
                     style="display:block"
                     data-ad-client="ca-pub-6389544196145251"
                     data-ad-slot="3131107512"
                     data-ad-format="vertical"></ins>
                <script>
                     (adsbygoogle = window.adsbygoogle || []).push({});
                </script>
            </div>
        </div>

        <!-- Main Content -->
        <div class="main-content">
"""

# Right Sidebar Ad (before closing page-wrapper)
right_sidebar = """        </div>

        <!-- Right Sidebar Ad -->
        <div class="sidebar-ad">
            <div class="ad-container">
                <div class="ad-label">Ad</div>
                <ins class="adsbygoogle"
                     style="display:block"
                     data-ad-client="ca-pub-6389544196145251"
                     data-ad-slot="3131107512"
                     data-ad-format="vertical"></ins>
                <script>
                     (adsbygoogle = window.adsbygoogle || []).push({});
                </script>
            </div>
        </div>
    </div>
"""

# Bottom Ad (for mobile)
bottom_ad = """
    <!-- Bottom Ad (Mobile only) -->
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

        # Check if sidebar ads already exist
        if 'sidebar-ad' in content and 'Left Sidebar Ad' in content:
            print(f'[SKIP] {filename} - da co sidebar ads')
            skipped += 1
            continue

        # Remove old top/bottom ads if they exist
        content = re.sub(r'<!-- Top Ad -->.*?</script>\s*</div>\s*', '', content, flags=re.DOTALL)

        # Remove old ad CSS but keep other styles
        content = re.sub(r'/\* Ad Styles \*/.*?@media \(max-width: 768px\) \{[^}]*\}\s*', '', content, flags=re.DOTALL)

        # 1. Add new sidebar CSS before </style>
        if '</style>' in content:
            content = content.replace('</style>', sidebar_css + '    </style>', 1)

        # 2. Add left sidebar and start main-content after <body>
        body_match = re.search(r'(<body[^>]*>)\s*', content)
        if body_match:
            insert_pos = body_match.end()
            content = content[:insert_pos] + '\n' + left_sidebar + content[insert_pos:]

        # 3. Add right sidebar and close page-wrapper before bottom ad or before </body>
        # First, remove the old bottom ad if exists
        content = re.sub(r'<!-- Bottom Ad -->.*?</div>\s*</body>', '</body>', content, flags=re.DOTALL)

        # Add right sidebar + bottom ad before </body>
        if '</body>' in content:
            content = content.replace('</body>', right_sidebar + bottom_ad + '</body>', 1)

        # Write the updated content
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f'[OK] Da them sidebar ads vao {filename}')
        processed += 1

    except Exception as e:
        print(f'[ERROR] Loi khi xu ly {filename}: {str(e)}')
        errors += 1

print(f'\nTONG KET:')
print(f'   Da xu ly: {processed} file')
print(f'   Da bo qua: {skipped} file')
print(f'   Loi: {errors} file')
