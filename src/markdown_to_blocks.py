from pprint import pprint

def markdown_to_blocks(md: str) -> list[str]:
    blocks = md.split("\n\n")
    return [block.strip(" ").strip("\n") for block in blocks if block]