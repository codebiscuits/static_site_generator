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

def generate_page(from_path, template_path, dest_path, base_path):

    with open(from_path, "r") as f:
        md = f.read()

    title = extract_title(md)
    html = markdown_to_html_node(md).to_html()

    with open(template_path, "r") as f:
        template = f.read()

    site = (
        template
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", html)
        .replace('href="/', f'href="{base_path}')
        .replace('src="/', f'src="{base_path}')
    )


    dest = Path(dest_path)
    dest.parent.mkdir(parents=True, exist_ok=True)

    with open(dest, "w") as f:
        f.write(site)

def generate_pages_recursive(source, template_path, dest, base_path):
    """Slightly modified version of recursive_dir_copy"""
    source = Path(source)
    dest = Path(dest)
    if source.is_file() and source.suffix == ".md":
        dest = dest.with_suffix(".html")
        generate_page(source, template_path, dest, base_path)
        return
    elif source.is_dir():
        contents = source.iterdir()
        if contents:
            for item in contents:
                new_dest = dest / item.stem
                if item.is_dir():
                    new_dest.mkdir(parents=True)
                generate_pages_recursive(item, template_path, new_dest, base_path)
    else:
        print(f"invalid source: {source}")
    return