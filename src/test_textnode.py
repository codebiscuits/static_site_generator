import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("first node", TextType.ITALIC)
        node2 = TextNode("second node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_url(self):
        test_url = "www.internet.com"
        node = TextNode("test", TextType.BOLD, "www.internet.com")
        self.assertEqual(test_url, node.url)

    def test_no_url(self):
        node = TextNode("test", TextType.PLAIN)
        self.assertEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()
