from markdown_to_blocks import *
from block_to_blocktype import *
from text_to_html import *
from text_to_textnodes import *
from htmlnode import LeafNode, ParentNode

def markdown_to_htmlnode(md):
    # this line creates a list of strings that are blocks of markdown text
    blocks = markdown_to_blocks(md)

    # now loop through that list of md strings
    nodes = []
    for block in blocks:
        # get the BlockType enum that classifies the block
        bt = block_to_blocktype(block)
        textnodes = text_to_textnodes(block)

        if bt == BlockType.HEADING:
            # count and strip leading '#' characters
            num_hashes = len(block) - len(block.lstrip("#"))
            tag = f"H{num_hashes}"
            block_txt = block.lstrip("#")
            sub_nodes = text_to_textnodes(block_txt)
            if len(sub_nodes) == 1:
                nodes.append(LeafNode(tag, textnodes[0].text))


