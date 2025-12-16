#!/usr/bin/env python3
"""
Script to fix all internal links in the website
"""

import os
import glob

def fix_links():
    # Fix links in root pages (about, contact, terms, faq)
    root_pages = ['about.html', 'contact.html', 'terms.html', 'faq.html']

    for page in root_pages:
        if not os.path.exists(page):
            print(f"[SKIP] {page} not found")
            continue

        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix all absolute paths to relative paths
        replacements = [
            ('href="/Index.html"', 'href="Index.html"'),
            ('href="/index.html"', 'href="Index.html"'),
            ('href="/contact.html"', 'href="contact.html"'),
            ('href="/about.html"', 'href="about.html"'),
            ('href="/faq.html"', 'href="faq.html"'),
            ('href="/terms.html"', 'href="terms.html"'),
            ('href="/blog.html"', 'href="blog.html"'),
            ('href="/feedback.html"', 'href="feedback.html"'),
            ('href="/privacy-policy.html"', 'href="privacy-policy.html"'),

            # Fix specific tool links
            ('href="/json-formatter.html"', 'href="json-formatter.html"'),
            ('href="/password-generator.html"', 'href="password-generator.html"'),
            ('href="/code-beautifier.html"', 'href="code-beautifier.html"'),
            ('href="/hash-generator.html"', 'href="hash-generator.html"'),
            ('href="/jwt-decoder.html"', 'href="jwt-decoder.html"'),
        ]

        for old, new in replacements:
            content = content.replace(old, new)

        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[OK] Fixed links in {page}")

    # Fix links in blog posts
    blog_posts = glob.glob('blog/*.html')

    for blog_post in blog_posts:
        with open(blog_post, 'r', encoding='utf-8') as f:
            content = f.read()

        # For blog posts, links should go up one level
        replacements = [
            ('href="/Index.html"', 'href="../Index.html"'),
            ('href="/index.html"', 'href="../Index.html"'),
            ('href="/blog.html"', 'href="../blog.html"'),
            ('href="/contact.html"', 'href="../contact.html"'),
            ('href="/about.html"', 'href="../about.html"'),
            ('href="/faq.html"', 'href="../faq.html"'),
            ('href="/terms.html"', 'href="../terms.html"'),
            ('href="/feedback.html"', 'href="../feedback.html"'),
            ('href="/privacy-policy.html"', 'href="../privacy-policy.html"'),

            # Fix tool links in blog posts
            ('href="/json-formatter.html"', 'href="../json-formatter.html"'),
            ('href="/password-generator.html"', 'href="../password-generator.html"'),
            ('href="/code-beautifier.html"', 'href="../code-beautifier.html"'),
            ('href="/hash-generator.html"', 'href="../hash-generator.html"'),
            ('href="/jwt-decoder.html"', 'href="../jwt-decoder.html"'),
        ]

        for old, new in replacements:
            content = content.replace(old, new)

        with open(blog_post, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[OK] Fixed links in {os.path.basename(blog_post)}")

    print(f"\n[SUCCESS] Fixed links in {len(root_pages)} root pages and {len(blog_posts)} blog posts!")

if __name__ == "__main__":
    os.chdir('Y:/zaptools')
    fix_links()
