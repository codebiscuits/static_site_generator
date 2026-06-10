from copy_files import copy_dir
from generate_page import generate_page


def main():

    copy_dir(
        "/home/ross/Documents/Coding/2026/static_site_generator/static",
        "/home/ross/Documents/Coding/2026/static_site_generator/public"
    )

    generate_page("content/index.md", "template.html", "public/index.html")

main()
