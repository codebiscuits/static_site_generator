from markdown_to_blocks import *
from block_to_blocktype import *
from text_to_html import *
from text_to_textnodes import *
from htmlnode import LeafNode, ParentNode, HTMLNode
from pprint import pprint

def text_to_children(text: str) -> list[HTMLNode]:
    output = []
    tnodes = text_to_textnodes(text)
    for tn in tnodes:
        output.append(text_node_to_html_node(tn))
    return output

def markdown_to_html_node(md):
    # this line creates a list of strings that are blocks of markdown text
    blocks = markdown_to_blocks(md.strip())
    # print("*")
    # print(blocks)
    # print("*")

    # now loop through that list of md strings
    nodes: list[HTMLNode] = []
    for block in blocks:
        # get the BlockType enum that classifies the block
        bt = block_to_blocktype(block)
        if bt == BlockType.HEADING:
            # count and strip leading '#' characters
            num_hashes = len(block) - len(block.lstrip("#"))
            tag = f"h{num_hashes}"
            block_txt = block[num_hashes+1:]
            nodes.append(LeafNode(tag, block_txt))

        elif bt == BlockType.PARAGRAPH:
            block = " ".join(block.split("\n"))
            nodes.append(ParentNode("p", text_to_children(block)))

        elif bt == BlockType.CODE:
            text = block[4:-3]
            print(f"Text: {text}")
            tn = TextNode(text, TextType.CODE)
            nodes.append(ParentNode("pre", text_node_to_html_node(tn)))

        elif bt == BlockType.QUOTE:
            nodes.append(ParentNode("quote", text_to_children(block[1:].lstrip())))

        elif bt == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            html_lines = []
            for line in lines:
                html_lines.append(ParentNode("li", text_to_children(line[2:])))
            nodes.append(ParentNode("ul", html_lines))

        elif bt == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            html_lines = []
            for line in lines:
                html_lines.append(ParentNode("li", text_to_children(line[3:])))
            nodes.append(ParentNode("ol", html_lines))

    return ParentNode("div", nodes)#.to_html()


if __name__ == "__main__":
    test = "some text with **bold** and _italic_ and `inline code` all together"

    print(markdown_to_html_node(test))
