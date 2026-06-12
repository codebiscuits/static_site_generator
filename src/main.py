from copy_files import copy_dir
from generate_page import generate_page, generate_pages_recursive
import sys


def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"
    print("base_path:", base_path)

    # First, copy everything from /static to /public
    copy_dir("/home/ross/Documents/Coding/2026/static_site_generator/static",
             "/home/ross/Documents/Coding/2026/static_site_generator/docs"
             )

    # Next, generate html files from the md files in /content
    generate_pages_recursive("/home/ross/Documents/Coding/2026/static_site_generator/content",
                             "/home/ross/Documents/Coding/2026/static_site_generator/template.html",
                             "/home/ross/Documents/Coding/2026/static_site_generator/docs",
                             base_path
                             )

main()
