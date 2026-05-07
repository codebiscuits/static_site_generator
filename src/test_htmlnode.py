import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_init(self):
        node = HTMLNode("p", "paragraph", None, {"test": "testing"})
        string = 'HTMLNode\np\nparagraph\nNone\n test="testing"'
        self.assertEqual(str(node), string)

    def test_props_to_html(self):
        node = HTMLNode("p", "paragraph", None, {"test": "testing"})
        self.assertEqual(node.props_to_html(), ' test="testing"')

    def test_no_props(self):
        node = HTMLNode("p", "paragraph")
        self.assertEqual(node.props_to_html(), "")

