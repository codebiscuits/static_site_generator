import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("p", "Hello, world!", {"test": "testing"})
        self.assertEqual(node.to_html(), '<p test="testing">Hello, world!</p>')

    def test_leaf_repr(self):
        node = LeafNode("p", "Hello, world!", {"test": "testing"})
        self.assertEqual(repr(node), 'HTMLNode\np\nHello, world!\n test="testing"')