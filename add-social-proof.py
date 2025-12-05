#!/usr/bin/env python3
"""
Script to add social proof elements to Index.html
"""

import re

# Read Index.html
with open('Y:/zaptools/Index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS link before </head>
if 'social-proof.css' not in content:
    content = content.replace(
        '</head>',
        '    <link rel="stylesheet" href="social-proof.css">\n</head>'
    )
    print("[OK] Added CSS link")

# 2. Add HTML elements before <div class="status">
social_proof_html = '''        <!-- Stats Counter -->
        <div class="stats-container">
            <div class="stat-box">
                <div class="stat-number">0</div>
                <div class="stat-label" id="statLabel1">Tools Used</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">0</div>
                <div class="stat-label" id="statLabel2">Users Today</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">0</div>
                <div class="stat-label" id="statLabel3">Happy Users</div>
            </div>
        </div>

        <!-- Trust Badges -->
        <div class="trust-badges">
            <div class="badge">
                <span class="badge-icon">[SUCCESS]</span>
                <span id="badge1">100% Free</span>
            </div>
            <div class="badge">
                <span class="badge-icon">🔒</span>
                <span id="badge2">Secure & Private</span>
            </div>
            <div class="badge">
                <span class="badge-icon">⚡</span>
                <span id="badge3">Lightning Fast</span>
            </div>
            <div class="badge">
                <span class="badge-icon">🚫</span>
                <span id="badge4">No Registration</span>
            </div>
        </div>

        <!-- Activity Feed -->
        <div class="activity-feed">
            <div class="activity-feed-title" id="activityTitle">Recent Activity</div>
            <div id="activityFeed"></div>
        </div>

        <!-- Testimonials -->
        <div class="testimonials">
            <div class="testimonial">
                <div class="testimonial-text" id="testimonial1">
                    "ZapTools saved me hours of work! The PDF converter is incredibly fast and easy to use."
                </div>
                <div class="testimonial-author">
                    <span class="testimonial-rating">⭐⭐⭐⭐⭐</span>
                    <span>- Sarah N., Designer</span>
                </div>
            </div>
            <div class="testimonial">
                <div class="testimonial-text" id="testimonial2">
                    "Best free tool suite I've found. Image compression works perfectly!"
                </div>
                <div class="testimonial-author">
                    <span class="testimonial-rating">⭐⭐⭐⭐⭐</span>
                    <span>- Mike T., Developer</span>
                </div>
            </div>
        </div>

'''

if 'stats-container' not in content:
    content = content.replace(
        '        <div class="status"',
        social_proof_html + '        <div class="status"'
    )
    print("[OK] Added social proof HTML elements")

# 3. Add JS script before </body>
if 'social-proof.js' not in content:
    content = content.replace(
        '</body>',
        '    <script src="social-proof.js"></script>\n</body>'
    )
    print("[OK] Added JavaScript")

# 4. Update langData to include new translations
if '"statLabel1"' not in content:
    # Add translations for stats
    lang_additions_vi = '''                    statLabel1: 'Công cụ đã dùng',
                    statLabel2: 'Người dùng hôm nay',
                    statLabel3: 'Người dùng hài lòng',
                    badge1: '100% Miễn phí',
                    badge2: 'Bảo mật & Riêng tư',
                    badge3: 'Siêu nhanh',
                    badge4: 'Không cần đăng ký',
                    activityTitle: 'Hoạt động gần đây',
                    testimonial1: '"ZapTools giúp tôi tiết kiệm hàng giờ làm việc! Công cụ chuyển đổi PDF cực kỳ nhanh và dễ dùng."',
                    testimonial2: '"Bộ công cụ miễn phí tốt nhất tôi từng thấy. Nén ảnh hoạt động hoàn hảo!"',
'''

    lang_additions_en = '''                    statLabel1: 'Tools Used',
                    statLabel2: 'Users Today',
                    statLabel3: 'Happy Users',
                    badge1: '100% Free',
                    badge2: 'Secure & Private',
                    badge3: 'Lightning Fast',
                    badge4: 'No Registration',
                    activityTitle: 'Recent Activity',
                    testimonial1: '"ZapTools saved me hours of work! The PDF converter is incredibly fast and easy to use."',
                    testimonial2: '"Best free tool suite I\'ve found. Image compression works perfectly!"',
'''

    content = re.sub(
        r"(vi: \{[^}]+status: [^\n]+\n)",
        r"\1" + lang_additions_vi,
        content
    )

    content = re.sub(
        r"(en: \{[^}]+status: [^\n]+\n)",
        r"\1" + lang_additions_en,
        content
    )

    # Add setLang updates
    set_lang_additions = '''                document.getElementById('statLabel1').textContent = langData[lang].statLabel1;
                document.getElementById('statLabel2').textContent = langData[lang].statLabel2;
                document.getElementById('statLabel3').textContent = langData[lang].statLabel3;
                document.getElementById('badge1').textContent = langData[lang].badge1;
                document.getElementById('badge2').textContent = langData[lang].badge2;
                document.getElementById('badge3').textContent = langData[lang].badge3;
                document.getElementById('badge4').textContent = langData[lang].badge4;
                document.getElementById('activityTitle').textContent = langData[lang].activityTitle;
                document.getElementById('testimonial1').textContent = langData[lang].testimonial1;
                document.getElementById('testimonial2').textContent = langData[lang].testimonial2;
'''

    content = re.sub(
        r"(document\.getElementById\('status'\)\.innerHTML = langData\[lang\]\.status;)",
        r"\1\n" + set_lang_additions,
        content
    )

    print("[OK] Added language translations")

# Write back
with open('Y:/zaptools/Index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n[SUCCESS] Successfully updated Index.html!")
print("\nAdded:")
print("  • Social proof CSS")
print("  • Stats counter with animation")
print("  • Trust badges")
print("  • Activity feed")
print("  • Testimonials")
print("  • Bilingual support")
