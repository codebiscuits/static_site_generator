from copy_files import copy_dir
from generate_page import generate_page, generate_pages_recursive


def main():
    # First, copy everything from /static to /public
    copy_dir("/home/ross/Documents/Coding/2026/static_site_generator/static",
             "/home/ross/Documents/Coding/2026/static_site_generator/public"
             )

    # Next, generate html files from the md files in /content
    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("/home/ross/Documents/Coding/2026/static_site_generator/content",
                             "/home/ross/Documents/Coding/2026/static_site_generator/template.html",
                             "/home/ross/Documents/Coding/2026/static_site_generator/public"
                             )

main()
