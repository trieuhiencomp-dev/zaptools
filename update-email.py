#!/usr/bin/env python3
"""
Script to update email address in all pages
"""

import os

def update_email_in_file(filename):
    """Update email in a single file"""
    if not os.path.exists(filename):
        print(f"[SKIP] {filename} not found")
        return False

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace old email with new email
    old_email = 'support@zaptools.org'
    new_email = 'trieuhiencomp@gmail.com'

    if old_email in content:
        content = content.replace(old_email, new_email)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[OK] Updated email in {filename}")
        return True
    else:
        print(f"[SKIP] No email found in {filename}")
        return False

def main():
    os.chdir('Y:/zaptools')

    files_to_update = [
        'faq.html',
        'terms.html',
        'about.html',
        'contact.html'
    ]

    updated_count = 0
    for filename in files_to_update:
        if update_email_in_file(filename):
            updated_count += 1

    print(f"\n[SUCCESS] Updated email in {updated_count} files!")
    print(f"New email: trieuhiencomp@gmail.com")

if __name__ == "__main__":
    main()
