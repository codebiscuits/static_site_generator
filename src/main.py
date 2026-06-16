from copy_files import copy_dir
from generate_page import generate_page, generate_pages_recursive
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"
    print("base_path:", base_path)

    # First, copy everything from /static into /docs
    copy_dir(
        BASE_DIR / "static",
        BASE_DIR / "docs",
    )

    # Then generate html from all markdown files in /content and put into /docs
    generate_pages_recursive(
        BASE_DIR / "content",
        BASE_DIR / "template.html",
        BASE_DIR / "docs",
        base_path,
    )

main()
