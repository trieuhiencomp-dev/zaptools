import os
import re

adsense_meta = '    <meta name="google-adsense-account" content="ca-pub-6389544196145251">'

html_files = [
    'barcode-generator.html', 'base64-encoder.html', 'blog.html', 'calculator.html',
    'case-converter.html', 'code-beautifier.html', 'code-minifier.html',
    'color-palette-extractor.html', 'color-picker.html', 'csv-to-json.html',
    'DanhSachTaoQR.html', 'diff-checker.html', 'email-validator.html', 'feedback.html',
    'file-history-widget.html', 'GiaiMaQR.html', 'hash-generator.html', 'html-encoder.html',
    'ImageCompress.html', 'ImageConvert.html', 'image-cropper.html', 'ImageResize.html',
    'image-tool.html', 'image-to-text.html', 'Index.html', 'ip-lookup.html',
    'json-formatter.html', 'json-to-xml.html', 'jwt-decoder.html', 'lorem-ipsum.html',
    'markdown-editor.html', 'meme-generator.html', 'MergePDFs.html', 'meta-tag-generator.html',
    'password-generator.html', 'PDFresize.html', 'PDFtoExcel.html', 'PDFtoImage.html',
    'pdf-tools.html', 'PDFtoPowerpoint.html', 'PDFtoWord.html', 'privacy-policy.html',
    'QRcode.html', 'QRcontact.html', 'QRevent.html', 'QRlinkweb.html', 'QRproduct.html',
    'QRwifi.html', 'random-name-generator.html', 'regex-tester.html', 'screenshot-tool.html',
    'social-proof-elements.html', 'SplitPDF.html', 'sql-formatter.html', 'stopwatch.html',
    'text-to-video.html', 'timestamp-converter.html', 'tts-tool.html', 'tts-tool-local.html',
    'unit-converter.html', 'url-encoder.html', 'url-shortener.html', 'uuid-generator.html',
    'word-counter.html', 'youtube-thumbnail-downloader.html'
]

processed = 0
skipped = 0
errors = 0

for filename in html_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'google-adsense-account' in content:
            print(f'[SKIP] {filename} - da co the meta AdSense')
            skipped += 1
            continue

        pattern = r'(<head>)'
        replacement = r'\1\n' + adsense_meta

        if '<head>' in content:
            new_content = re.sub(pattern, replacement, content, count=1)

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f'[OK] Da them vao {filename}')
            processed += 1
        else:
            print(f'[WARNING] Khong tim thay the <head> trong {filename}')
            errors += 1

    except Exception as e:
        print(f'[ERROR] Loi khi xu ly {filename}: {str(e)}')
        errors += 1

print(f'\nTONG KET:')
print(f'   Da xu ly: {processed} file')
print(f'   Da bo qua: {skipped} file')
print(f'   Loi: {errors} file')
