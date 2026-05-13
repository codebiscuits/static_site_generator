import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):

    test_nodes = [
        TextNode("This contains plain text", TextType.TEXT),
        TextNode("This contains **bold** text", TextType.TEXT),
        TextNode("This contains _italic_ text", TextType.TEXT),
        TextNode("This contains `code` text", TextType.TEXT),
        TextNode("This contains invalid **bold text", TextType.TEXT),
        TextNode("This contains invalid _italic text", TextType.TEXT),
        TextNode("This contains invalid `code text", TextType.TEXT),
        TextNode("This _contains **nested** bold_ text", TextType.TEXT),
    ]

    def test_text(self):
        output = split_nodes_delimiter(self.test_nodes[0:1], "_", TextType.ITALIC)
        self.assertEqual(output, self.test_nodes[0:1])

    def test_bold(self):
        output = split_nodes_delimiter(self.test_nodes[1:2], "**", TextType.BOLD)
        self.assertEqual(
            output,
            [
                TextNode("This contains ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ]
        )

    def test_italic(self):
        output = split_nodes_delimiter(self.test_nodes[2:3], "_", TextType.ITALIC)
        self.assertEqual(
            output,
            [
                TextNode("This contains ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ]
        )

    def test_code(self):
        output = split_nodes_delimiter(self.test_nodes[3:4], "`", TextType.CODE)
        self.assertEqual(
            output,
            [
                TextNode("This contains ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text", TextType.TEXT),
            ]
        )

    def test_1_bold(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter(self.test_nodes[4:5], "**", TextType.BOLD)

    def test_1_italic(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter(self.test_nodes[5:6], "_", TextType.ITALIC)

    def test_1_code(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter(self.test_nodes[6:7], "`", TextType.CODE)

    def test_all_valid(self):
        first_output = split_nodes_delimiter(self.test_nodes[:4], "**", TextType.BOLD)
        second_output = split_nodes_delimiter(first_output, "_", TextType.ITALIC)
        final_output = split_nodes_delimiter(second_output, "`", TextType.CODE)
        self.assertEqual(
            final_output,
            [
                TextNode("This contains plain text", TextType.TEXT, None),
                TextNode("This contains ", TextType.TEXT, None),
                TextNode("bold", TextType.BOLD, None),
                TextNode(" text", TextType.TEXT, None),
                TextNode("This contains ", TextType.TEXT, None),
                TextNode("italic", TextType.ITALIC, None),
                TextNode(" text", TextType.TEXT, None),
                TextNode("This contains ", TextType.TEXT, None),
                TextNode("code", TextType.CODE, None),
                TextNode(" text", TextType.TEXT, None)
            ]
        )