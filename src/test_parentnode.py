import unittest
from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    # These first two tests cover both valid types for the children argument and the .to_html method
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_children(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", None)
            parent_node.to_html()

    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError):
            child_node = LeafNode("span", "child")
            parent_node = ParentNode(None, [child_node])
            parent_node.to_html()

    # children must either be an htmlnode or a list of htmlnodes
    def test_to_html_children_string(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", "not an htmlnode")
            parent_node.to_html()

    def test_to_html_children_int(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", 1)
            parent_node.to_html()

    def test_to_html_children_None(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", None)
            parent_node.to_html()
