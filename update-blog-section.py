#!/usr/bin/env python3
"""
Script to update blog section in Index.html with latest blog posts
"""

def update_blog_section():
    with open('Index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the blog post 4 and add new blog posts after it
    old_blog_4 = '''                <!-- Blog Post 4 -->
                <a href="blog/qr-codes-for-business.html" class="blog-card">
                    <div class="blog-card-header">
                        <div class="blog-icon">📱</div>
                        <span class="blog-category" id="blogCat4">Doanh nghiệp</span>
                    </div>
                    <div class="blog-title" id="blogTitle4">QR Code Cho Doanh Nghiệp</div>
                    <div class="blog-excerpt" id="blogExcerpt4">
                        Học cách tạo và sử dụng QR code hiệu quả cho phát triển doanh nghiệp!
                    </div>
                    <div class="blog-meta">
                        <span class="blog-date">📅 <span id="blogDate4">13 Tháng 1, 2025</span></span>
                        <span class="blog-read-time">⏱️ <span id="blogRead4">6 phút</span></span>
                    </div>
                </a>'''

    new_blog_posts = '''                <!-- Blog Post 4 -->
                <a href="blog/qr-codes-for-business.html" class="blog-card">
                    <div class="blog-card-header">
                        <div class="blog-icon">📱</div>
                        <span class="blog-category" id="blogCat4">Doanh nghiệp</span>
                    </div>
                    <div class="blog-title" id="blogTitle4">QR Code Cho Doanh Nghiệp</div>
                    <div class="blog-excerpt" id="blogExcerpt4">
                        Học cách tạo và sử dụng QR code hiệu quả cho phát triển doanh nghiệp!
                    </div>
                    <div class="blog-meta">
                        <span class="blog-date">📅 <span id="blogDate4">13 Tháng 1, 2025</span></span>
                        <span class="blog-read-time">⏱️ <span id="blogRead4">6 phút</span></span>
                    </div>
                </a>

                <!-- Blog Post 5 - NEW -->
                <a href="blog/top-10-json-formatters-2025.html" class="blog-card">
                    <div class="blog-card-header">
                        <div class="blog-icon">💻</div>
                        <span class="blog-category" id="blogCat5">Developer Tools</span>
                    </div>
                    <div class="blog-title" id="blogTitle5">Top 10 JSON Formatters 2025</div>
                    <div class="blog-excerpt" id="blogExcerpt5">
                        Compare the best JSON formatters and find the perfect tool for your development workflow!
                    </div>
                    <div class="blog-meta">
                        <span class="blog-date">📅 <span id="blogDate5">Jan 15, 2025</span></span>
                        <span class="blog-read-time">⏱️ <span id="blogRead5">8 min</span></span>
                    </div>
                </a>

                <!-- Blog Post 6 - NEW -->
                <a href="blog/jwt-tokens-explained-2025.html" class="blog-card">
                    <div class="blog-card-header">
                        <div class="blog-icon">🔐</div>
                        <span class="blog-category" id="blogCat6">Developer Tools</span>
                    </div>
                    <div class="blog-title" id="blogTitle6">JWT Tokens Explained</div>
                    <div class="blog-excerpt" id="blogExcerpt6">
                        Complete guide to understanding JWT authentication, security best practices, and how to decode JWTs!
                    </div>
                    <div class="blog-meta">
                        <span class="blog-date">📅 <span id="blogDate6">Jan 16, 2025</span></span>
                        <span class="blog-read-time">⏱️ <span id="blogRead6">10 min</span></span>
                    </div>
                </a>

                <!-- Blog Post 7 - NEW -->
                <a href="blog/password-security-guide-2025.html" class="blog-card">
                    <div class="blog-card-header">
                        <div class="blog-icon">🔒</div>
                        <span class="blog-category" id="blogCat7">Security</span>
                    </div>
                    <div class="blog-title" id="blogTitle7">Password Security Guide 2025</div>
                    <div class="blog-excerpt" id="blogExcerpt7">
                        Master password security! Learn to create unbreakable passwords, use 2FA, and protect yourself from attacks!
                    </div>
                    <div class="blog-meta">
                        <span class="blog-date">📅 <span id="blogDate7">Jan 17, 2025</span></span>
                        <span class="blog-read-time">⏱️ <span id="blogRead7">12 min</span></span>
                    </div>
                </a>

                <!-- Blog Post 8 - NEW -->
                <a href="blog/best-image-formats-for-web-2025.html" class="blog-card">
                    <div class="blog-card-header">
                        <div class="blog-icon">🖼️</div>
                        <span class="blog-category" id="blogCat8">Image Tools</span>
                    </div>
                    <div class="blog-title" id="blogTitle8">Best Image Formats for Web 2025</div>
                    <div class="blog-excerpt" id="blogExcerpt8">
                        PNG vs JPG vs WebP vs AVIF - Learn which image format to use for optimal performance and quality!
                    </div>
                    <div class="blog-meta">
                        <span class="blog-date">📅 <span id="blogDate8">Jan 18, 2025</span></span>
                        <span class="blog-read-time">⏱️ <span id="blogRead8">9 min</span></span>
                    </div>
                </a>'''

    if old_blog_4 in content:
        content = content.replace(old_blog_4, new_blog_posts)
        print("[OK] Updated blog section with 4 new posts (total: 8 posts)")
    else:
        print("[WARNING] Blog section pattern not found")

    # Save updated content
    with open('Index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("[SUCCESS] Index.html blog section updated!")

if __name__ == "__main__":
    update_blog_section()
