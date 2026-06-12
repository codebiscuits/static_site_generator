import unittest
from markdown_to_htmlnode import *

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_h1(self):
        md = "# Heading 1"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1></div>"
        )

    def test_h2(self):
        md = "## Heading 2"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Heading 2</h2></div>"
        )

    def test_h3(self):
        md = "### Heading 3"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Heading 3</h3></div>"
        )

    def test_h4(self):
        md = "#### Heading 4"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>Heading 4</h4></div>"
        )

    def test_h5(self):
        md = "##### Heading 5"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5>Heading 5</h5></div>"
        )

    def test_h6(self):
        md = "###### Heading 6"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>Heading 6</h6></div>"
        )

    def test_ul(self):
        md = """
- a
- b
- c
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>a</li><li>b</li><li>c</li></ul></div>"
        )

    def test_ol(self):
        md = """
1. a
2. b
3. c
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>a</li><li>b</li><li>c</li></ol></div>"
        )

    def test_quote(self):
        md = """
> this is a block quote

>this is too
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>this is a block quote</blockquote><blockquote>this is too</blockquote></div>"
        )

    def test_inline(self):
        md = "some text with **bold** and _italic_ and `inline code` all together"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>some text with <b>bold</b> and <i>italic</i> and <code>inline code</code> all together</p></div>"
        )

    def test_multiline(self):
        md = """
this is a line
and so is this
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>this is a line and so is this</p></div>"
        )

    def test_straight_paragraph(self):
        md = "This is a paragraph with no children."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a paragraph with no children.</p></div>"
        )

    def test_empty_md(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div></div>"
        )