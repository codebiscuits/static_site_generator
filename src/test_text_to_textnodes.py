import unittest
from text_to_textnodes import text_to_textnodes
from split_nodes import *
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestTextToTextNodes(unittest.TestCase):
    def test_all_nodes(self):
        text_in = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        out = text_to_textnodes(text_in)

        self.assertListEqual(
            out,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

    def test_empty_text(self):
        out = text_to_textnodes("")
        self.assertListEqual(out, [])

