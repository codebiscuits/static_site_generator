from enum import Enum
from pprint import pprint

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_blocktype(block: str) -> BlockType:
    block_type = BlockType.PARAGRAPH
    match block[0]:
        case "#":
            prefix = block.split(" ")[0]
            if len(prefix) <= 6 and set(prefix) == {"#"}:
                block_type = BlockType.HEADING
        case "`":
            if block[:4] == "```\n" and block[-4:] == "\n```":
                block_type = BlockType.CODE
        case ">":
            block_type = BlockType.QUOTE
        case "-":
            lines = block.split("\n")
            if all(l[:2] == "- " for l in lines):
                block_type = BlockType.UNORDERED_LIST
        case "1":
            lines = enumerate(block.split("\n"))
            formatted_lines = [(str(l[0]+1)+". ", l[1][:3]) for l in lines]
            if all(fl[0] == fl[1] for fl in formatted_lines):
                block_type = BlockType.ORDERED_LIST

    return block_type

if __name__ == "__main__":
    print("headings")
    print(block_to_blocktype("# Heading"))
    print(block_to_blocktype("## Heading"))
    print(block_to_blocktype("### Heading"))
    print(block_to_blocktype("#### Heading"))
    print(block_to_blocktype("##### Heading"))
    print(block_to_blocktype("###### Heading"))
    print(block_to_blocktype("####### bad Heading"))
    print("ol")
    print(block_to_blocktype("1. valid ordered list\n2. Second item\n3. Third item"))
    print(block_to_blocktype("1invalid ordered list\n2. Second item\n3. Third item"))
    print(block_to_blocktype("1. invalid ordered list\n3. Second item\n3. Third item"))
    print("ul")
    print(block_to_blocktype("- valid unordered list\n- Second item\n- Third item"))
    print(block_to_blocktype("-invalid unordered list\n- Second item\n- Third item"))
    print(block_to_blocktype("- valid unordered list\n+ Second item\n- Third item"))
    print("quote")
    print(block_to_blocktype("> This is a valid quote"))
    print(block_to_blocktype(">This is a valid quote"))
    print("code")
    print(block_to_blocktype("```\nprint('valid code block')\n```"))
    print(block_to_blocktype("```print('invalid code block')\n```"))
    print(block_to_blocktype("``\nprint('invalid code block')\n```"))
    print(block_to_blocktype("```\nprint('invalid code block')\n``"))
    print(block_to_blocktype("```\nprint('invalid code block')```"))
