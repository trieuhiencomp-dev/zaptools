#!/usr/bin/env python3
"""
Generate OG Images for ZapTools
Requires: pip install pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

# OG Image standard size
OG_WIDTH = 1200
OG_HEIGHT = 630

# ZapTools brand colors (from gradient)
COLOR_PRIMARY = (102, 126, 234)  # #667eea
COLOR_SECONDARY = (118, 75, 162)  # #764ba2
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (74, 222, 128)  # #4ade80

def create_gradient_background(width, height):
    """Create gradient background matching ZapTools style"""
    image = Image.new('RGB', (width, height), COLOR_PRIMARY)
    draw = ImageDraw.Draw(image)

    # Create diagonal gradient
    for y in range(height):
        for x in range(width):
            # Calculate gradient position (0 to 1)
            ratio = (x + y) / (width + height)

            # Interpolate between primary and secondary colors
            r = int(COLOR_PRIMARY[0] + (COLOR_SECONDARY[0] - COLOR_PRIMARY[0]) * ratio)
            g = int(COLOR_PRIMARY[1] + (COLOR_SECONDARY[1] - COLOR_PRIMARY[1]) * ratio)
            b = int(COLOR_PRIMARY[2] + (COLOR_SECONDARY[2] - COLOR_PRIMARY[2]) * ratio)

            draw.point((x, y), fill=(r, g, b))

    return image

def add_rounded_rectangle(draw, xy, radius, fill):
    """Draw a rounded rectangle"""
    x1, y1, x2, y2 = xy
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)
    draw.pieslice([x1, y1, x1 + radius * 2, y1 + radius * 2], 180, 270, fill=fill)
    draw.pieslice([x2 - radius * 2, y1, x2, y1 + radius * 2], 270, 360, fill=fill)
    draw.pieslice([x1, y2 - radius * 2, x1 + radius * 2, y2], 90, 180, fill=fill)
    draw.pieslice([x2 - radius * 2, y2 - radius * 2, x2, y2], 0, 90, fill=fill)

def create_og_image(title, subtitle, icon, filename, category="tool"):
    """Create an OG image with title, subtitle and icon"""

    # Create base image with gradient
    img = create_gradient_background(OG_WIDTH, OG_HEIGHT)
    draw = ImageDraw.Draw(img)

    # Add semi-transparent overlay for better text readability
    overlay = Image.new('RGBA', (OG_WIDTH, OG_HEIGHT), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)

    # Add rounded rectangle card
    card_margin = 80
    card_coords = (card_margin, card_margin, OG_WIDTH - card_margin, OG_HEIGHT - card_margin)
    add_rounded_rectangle(overlay_draw, card_coords, 30, (255, 255, 255, 25))

    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)

    # Try to load fonts (with fallbacks)
    try:
        # Try to use Arial/Helvetica (common on most systems)
        title_font = ImageFont.truetype("arial.ttf", 80)
        subtitle_font = ImageFont.truetype("arial.ttf", 40)
        icon_font = ImageFont.truetype("arial.ttf", 120)
        brand_font = ImageFont.truetype("arialbd.ttf", 45)
    except:
        try:
            title_font = ImageFont.truetype("Arial.ttf", 80)
            subtitle_font = ImageFont.truetype("Arial.ttf", 40)
            icon_font = ImageFont.truetype("Arial.ttf", 120)
            brand_font = ImageFont.truetype("Arial.ttf", 45)
        except:
            # Fallback to default font
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            icon_font = ImageFont.load_default()
            brand_font = ImageFont.load_default()
            print(f"Warning: Using default font for {filename}")

    # Draw icon/emoji at top
    icon_bbox = draw.textbbox((0, 0), icon, font=icon_font)
    icon_width = icon_bbox[2] - icon_bbox[0]
    icon_x = (OG_WIDTH - icon_width) // 2
    draw.text((icon_x, 120), icon, fill=COLOR_WHITE, font=icon_font)

    # Draw title (centered, with text wrapping if needed)
    title_y = 270

    # Simple text wrapping
    words = title.split()
    lines = []
    current_line = []

    for word in words:
        current_line.append(word)
        test_line = ' '.join(current_line)
        bbox = draw.textbbox((0, 0), test_line, font=title_font)
        line_width = bbox[2] - bbox[0]

        if line_width > OG_WIDTH - 200:
            current_line.pop()
            lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    # Draw each line centered
    for i, line in enumerate(lines[:2]):  # Max 2 lines
        bbox = draw.textbbox((0, 0), line, font=title_font)
        line_width = bbox[2] - bbox[0]
        line_x = (OG_WIDTH - line_width) // 2
        draw.text((line_x, title_y + i * 90), line, fill=COLOR_WHITE, font=title_font)

    # Draw subtitle
    subtitle_y = title_y + len(lines) * 90 + 20
    bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = bbox[2] - bbox[0]
    subtitle_x = (OG_WIDTH - subtitle_width) // 2
    draw.text((subtitle_x, subtitle_y), subtitle, fill=COLOR_WHITE, font=subtitle_font, stroke_width=1, stroke_fill=(0, 0, 0))

    # Draw ZapTools brand at bottom
    brand_text = "⚡ ZapTools.org"
    bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
    brand_width = bbox[2] - bbox[0]
    brand_x = (OG_WIDTH - brand_width) // 2
    draw.text((brand_x, OG_HEIGHT - 100), brand_text, fill=COLOR_GREEN, font=brand_font)

    # Save image
    img.save(filename, 'PNG', optimize=True, quality=95)
    print(f"[OK] Created: {filename}")

def main():
    """Generate all OG images"""

    print("Generating OG Images for ZapTools...\n")

    # Create output directory if not exists
    os.makedirs("og-images", exist_ok=True)

    images = [
        # Main pages
        {
            "title": "ZapTools",
            "subtitle": "Lightning-Fast Online Tools",
            "icon": "⚡",
            "filename": "og-images/og-image.png"
        },
        {
            "title": "Unit Converter",
            "subtitle": "Convert Length, Weight, Temperature & More",
            "icon": "📏",
            "filename": "og-images/og-image-unit-converter.png"
        },
        {
            "title": "Image Tools",
            "subtitle": "Compress, Resize, Convert Images",
            "icon": "🖼️",
            "filename": "og-images/og-image-image-tool.png"
        },
        {
            "title": "PDF Tools",
            "subtitle": "Convert, Merge, Split PDFs",
            "icon": "📄",
            "filename": "og-images/og-image-pdf-tools.png"
        },
        {
            "title": "QR Code Tools",
            "subtitle": "Generate & Decode QR Codes",
            "icon": "📱",
            "filename": "og-images/og-image-QRcode.png"
        },
        {
            "title": "ZapTools Blog",
            "subtitle": "Tips, Tutorials & Guides",
            "icon": "📝",
            "filename": "og-images/og-image-blog.png"
        },

        # Blog posts
        {
            "title": "Unit Converter Guide",
            "subtitle": "How to Convert Units Like a Pro",
            "icon": "📏",
            "filename": "og-images/og-image-unit-converter-guide.png"
        },
        {
            "title": "Image Compression Tips",
            "subtitle": "10 Tips for Perfect Compression",
            "icon": "🖼️",
            "filename": "og-images/og-image-image-compression-tips.png"
        },
        {
            "title": "QR Codes for Business",
            "subtitle": "Boost Your Marketing with QR Codes",
            "icon": "📱",
            "filename": "og-images/og-image-qr-codes-for-business.png"
        },

        # Specific tools
        {
            "title": "Image Compress",
            "subtitle": "Reduce Image Size Without Quality Loss",
            "icon": "🗜️",
            "filename": "og-images/og-image-ImageCompress.png"
        },
        {
            "title": "Image Resize",
            "subtitle": "Resize Photos & Images Online",
            "icon": "↔️",
            "filename": "og-images/og-image-ImageResize.png"
        },
        {
            "title": "Image Convert",
            "subtitle": "Convert JPG, PNG, WebP Formats",
            "icon": "🔄",
            "filename": "og-images/og-image-ImageConvert.png"
        },
        {
            "title": "PDF to Word",
            "subtitle": "Convert PDF to DOCX Online",
            "icon": "📄",
            "filename": "og-images/og-image-PDFtoWord.png"
        },
        {
            "title": "Merge PDFs",
            "subtitle": "Combine Multiple PDFs into One",
            "icon": "📑",
            "filename": "og-images/og-image-MergePDFs.png"
        },
        {
            "title": "Split PDF",
            "subtitle": "Split PDF Pages Online",
            "icon": "✂️",
            "filename": "og-images/og-image-SplitPDF.png"
        },

        # Additional tools
        {
            "title": "PDF to Excel",
            "subtitle": "Convert PDF to XLSX Online",
            "icon": "📊",
            "filename": "og-images/og-image-PDFtoExcel.png"
        },
        {
            "title": "PDF to Image",
            "subtitle": "Convert PDF to JPG/PNG",
            "icon": "🖼️",
            "filename": "og-images/og-image-PDFtoImage.png"
        },
        {
            "title": "PDF to PowerPoint",
            "subtitle": "Convert PDF to PPTX Online",
            "icon": "📊",
            "filename": "og-images/og-image-PDFtoPowerpoint.png"
        },
        {
            "title": "PDF Resize",
            "subtitle": "Resize PDF Pages Online",
            "icon": "📐",
            "filename": "og-images/og-image-PDFresize.png"
        },
        {
            "title": "WiFi QR Code",
            "subtitle": "Share WiFi Password Instantly",
            "icon": "📶",
            "filename": "og-images/og-image-QRwifi.png"
        },
        {
            "title": "Contact QR Code",
            "subtitle": "Digital Business Card QR",
            "icon": "👤",
            "filename": "og-images/og-image-QRcontact.png"
        },
        {
            "title": "Event QR Code",
            "subtitle": "Calendar Event QR Code",
            "icon": "📅",
            "filename": "og-images/og-image-QRevent.png"
        },
        {
            "title": "Product QR Code",
            "subtitle": "Product Information QR",
            "icon": "📦",
            "filename": "og-images/og-image-QRproduct.png"
        },
        {
            "title": "URL QR Code",
            "subtitle": "Link QR Code Generator",
            "icon": "🔗",
            "filename": "og-images/og-image-QRlinkweb.png"
        },
        {
            "title": "QR Code Scanner",
            "subtitle": "Decode QR Codes Online",
            "icon": "🔍",
            "filename": "og-images/og-image-GiaiMaQR.png"
        },
        {
            "title": "Create QR Codes",
            "subtitle": "Choose Your QR Code Type",
            "icon": "✨",
            "filename": "og-images/og-image-DanhSachTaoQR.png"
        },
        {
            "title": "Privacy Policy",
            "subtitle": "Your Privacy Matters to Us",
            "icon": "🔒",
            "filename": "og-images/og-image-privacy-policy.png"
        },

        # New Tier 1 Tools
        {
            "title": "Word Counter",
            "subtitle": "Count Words, Characters & More",
            "icon": "📝",
            "filename": "og-images/og-image-word-counter.png"
        },
        {
            "title": "Password Generator",
            "subtitle": "Create Strong Secure Passwords",
            "icon": "🔐",
            "filename": "og-images/og-image-password-generator.png"
        },
        {
            "title": "Color Picker",
            "subtitle": "HEX, RGB, HSL Converter",
            "icon": "🎨",
            "filename": "og-images/og-image-color-picker.png"
        },
        {
            "title": "JSON Formatter",
            "subtitle": "Validate, Format & Minify JSON",
            "icon": "📋",
            "filename": "og-images/og-image-json-formatter.png"
        },

        # Tier 2 Tools
        {
            "title": "Base64 Encoder",
            "subtitle": "Encode & Decode Base64",
            "icon": "🔐",
            "filename": "og-images/og-image-base64-encoder.png"
        },
        {
            "title": "Hash Generator",
            "subtitle": "MD5, SHA-1, SHA-256, SHA-512",
            "icon": "#️⃣",
            "filename": "og-images/og-image-hash-generator.png"
        },
        {
            "title": "Case Converter",
            "subtitle": "UPPER, lower, Title, camelCase",
            "icon": "🔤",
            "filename": "og-images/og-image-case-converter.png"
        },
        {
            "title": "URL Encoder",
            "subtitle": "Encode & Decode URLs",
            "icon": "🔗",
            "filename": "og-images/og-image-url-encoder.png"
        },
    ]

    # Generate all images
    for img_config in images:
        try:
            create_og_image(
                title=img_config["title"],
                subtitle=img_config["subtitle"],
                icon=img_config["icon"],
                filename=img_config["filename"]
            )
        except Exception as e:
            print(f"[ERROR] Error creating {img_config['filename']}: {str(e)}")

    print(f"\n[SUCCESS] Successfully generated {len(images)} OG images!")
    print(f"[SUCCESS] Images saved in: og-images/ folder")
    print(f"\nNext steps:")
    print("1. Review images in og-images/ folder")
    print("2. Upload images to your server")
    print("3. Update OG image URLs in HTML files")

if __name__ == '__main__':
    main()
