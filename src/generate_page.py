from markdown_to_blocks import *
from markdown_to_htmlnode import *
from htmlnode import *
from pathlib import Path


def extract_title(md: str) -> str:
    blocks = markdown_to_blocks(md)
    title = ""
    for block in blocks:
        if block[:2] == "# ":
            return block.lstrip("# ").strip()
    raise Exception("Source has no title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")

    with open(from_path, "r") as f:
        md = f.read()

    title = extract_title(md)
    html = markdown_to_html_node(md).to_html()

    with open(template_path, "r") as f:
        template = f.read()

    site = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dest = Path(dest_path)
    dest.parent.mkdir(parents=True, exist_ok=True)

    with open(dest, "w") as f:
        f.write(site)