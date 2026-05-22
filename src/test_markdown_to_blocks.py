import unittest
from markdown_to_blocks import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        self.assertEqual(
            markdown_to_blocks("first block\n\nsecond block  \n\n\nthird block"),
            ["first block", "second block", "third block"]
        )

    def test_empty_markdown(self):
        self.assertEqual(markdown_to_blocks(""), [])