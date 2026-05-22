from extract_markdown import *
import unittest

class TestExtractMarkdownImage(unittest.TestCase):
    def test_extract_markdown_image(self):
        self.assertEqual(extract_markdown_images("Testing ![image](image.jpg)"), [("image", "image.jpg")])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

class TestExtractMarkdownLink(unittest.TestCase):
    def test_extract_markdown_link(self):
        self.assertEqual(extract_markdown_links("Testing [test](test.jpg)"), [("test", "test.jpg")])

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an ![image](image.png) This is text with a [link](https://www.google.com)"
        )
        self.assertListEqual(
            [("link", "https://www.google.com")], matches)