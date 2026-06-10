import unittest
from generate_page import *

class GeneratePageTest(unittest.TestCase):
    def test_h1(self):
        md = "# This is a valid Header"
        self.assertEqual(
            extract_title(md),
            "This is a valid Header"
        )

    def test_invalid_h1(self):
        md = "#This is not a valid header"
        self.assertRaises(Exception, extract_title, md)

    def test_several_blocks(self):
        md = "# Valid Header\n\nparagraph paragraph paragraph paragraph paragraph paragraph paragraph \n\n```\ncode code code code \n```"
        self.assertEqual(
            extract_title(md),
            "Valid Header"
        )

    def test_h2_first(self):
        md = "## This shouldn't really happen\n\n# But I Should Test It Anyway"
        self.assertEqual(
            extract_title(md),
            "But I Should Test It Anyway"
        )