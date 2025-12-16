#!/usr/bin/env python3
"""
Script to update Index.html with footer links and new blog posts
"""

def update_index_html():
    with open('Index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace footer
    old_footer = """        <footer>
            &copy; 2025 ZapTools.org • Built with ❤️"""

    new_footer = """        <footer style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.2);">
            <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 1.5rem; flex-wrap: wrap; font-size: 0.9rem;">
                <a href="about.html" style="color: white; text-decoration: none; opacity: 0.8; transition: opacity 0.3s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.8'">About</a>
                <a href="contact.html" style="color: white; text-decoration: none; opacity: 0.8; transition: opacity 0.3s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.8'">Contact</a>
                <a href="faq.html" style="color: white; text-decoration: none; opacity: 0.8; transition: opacity 0.3s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.8'">FAQ</a>
                <a href="blog.html" style="color: white; text-decoration: none; opacity: 0.8; transition: opacity 0.3s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.8'">Blog</a>
                <a href="feedback.html" style="color: white; text-decoration: none; opacity: 0.8; transition: opacity 0.3s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.8'">Feedback</a>
                <a href="privacy-policy.html" style="color: white; text-decoration: none; opacity: 0.8; transition: opacity 0.3s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.8'">Privacy</a>
                <a href="terms.html" style="color: white; text-decoration: none; opacity: 0.8; transition: opacity 0.3s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.8'">Terms</a>
            </div>
            <div style="text-align: center; opacity: 0.7;">
                &copy; 2025 ZapTools.org • Built with ❤️
            </div>"""

    if old_footer in content:
        content = content.replace(old_footer, new_footer)
        print("[OK] Updated footer with navigation links")
    else:
        print("[WARNING] Footer pattern not found, skipping footer update")

    # Save updated content
    with open('Index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("[SUCCESS] Index.html updated successfully!")

if __name__ == "__main__":
    update_index_html()
