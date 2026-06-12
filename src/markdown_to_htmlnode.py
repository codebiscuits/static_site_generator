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
    if md == "":
        return LeafNode("div", "")
    blocks = markdown_to_blocks(md.strip())

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
            children = text_to_children(block)
            if children:
                nodes.append(ParentNode("p", children))
            else:
                nodes.append(LeafNode("p", block))

        elif bt == BlockType.CODE:
            text = block[4:-3]
            # print(f"Text: {text}")
            tn = TextNode(text, TextType.CODE)
            nodes.append(ParentNode("pre", text_node_to_html_node(tn)))

        elif bt == BlockType.QUOTE:
            children = text_to_children(block[1:].lstrip())
            if children:
                nodes.append(ParentNode("blockquote", children))
            else:
                nodes.append(LeafNode("blockquote", block))

        elif bt == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            html_lines = []
            for line in lines:
                children = text_to_children(line[2:])
                if children:
                    html_lines.append(ParentNode("li", children))
                else:
                    html_lines.append(LeafNode("li", line[2:]))
            nodes.append(ParentNode("ul", html_lines))

        elif bt == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            html_lines = []
            for line in lines:
                children = text_to_children(line[3:])
                if children:
                    html_lines.append(ParentNode("li", children))
                else:
                    html_lines.append(LeafNode("li", line[3:]))
            nodes.append(ParentNode("ol", html_lines))

    return ParentNode("div", nodes)#.to_html()


if __name__ == "__main__":
    test = "some text with **bold** and _italic_ and `inline code` all together"

    print(markdown_to_html_node(test))
