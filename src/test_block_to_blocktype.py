import unittest
from block_to_blocktype import *

class TestBlockToBlockType(unittest.TestCase):
    def test_headings(self):
        self.assertEqual(block_to_blocktype("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_blocktype("## Heading"), BlockType.HEADING)
        self.assertEqual(block_to_blocktype("### Heading"), BlockType.HEADING)
        self.assertEqual(block_to_blocktype("#### Heading"), BlockType.HEADING)
        self.assertEqual(block_to_blocktype("##### Heading"), BlockType.HEADING)
        self.assertEqual(block_to_blocktype("###### Heading"), BlockType.HEADING)
        self.assertNotEqual(block_to_blocktype("####### Heading"), BlockType.HEADING)

    def test_code(self):
        self.assertEqual(block_to_blocktype("```\nprint('valid code block')\n```"), BlockType.CODE)
        self.assertNotEqual(block_to_blocktype("```print('invalid code block')\n```"), BlockType.CODE)
        self.assertNotEqual(block_to_blocktype("``\nprint('invalid code block')\n```"), BlockType.CODE)
        self.assertNotEqual(block_to_blocktype("```\nprint('invalid code block')\n``"), BlockType.CODE)
        self.assertNotEqual(block_to_blocktype("```\nprint('invalid code block')```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_blocktype("> This is a valid quote"), BlockType.QUOTE)
        self.assertEqual(block_to_blocktype(">This is a valid quote"), BlockType.QUOTE)

    def test_ordered_list(self):
        self.assertEqual(
            block_to_blocktype("1. valid ordered list\n2. Second item\n3. Third item"),
            BlockType.ORDERED_LIST
        )
        self.assertNotEqual(
            block_to_blocktype("1invalid ordered list\n2. Second item\n3. Third item"),
            BlockType.ORDERED_LIST
        )
        self.assertNotEqual(
            block_to_blocktype("1. invalid ordered list\n3. Second item\n3. Third item"),
            BlockType.ORDERED_LIST
        )

    def test_unordered_list(self):
        self.assertEqual(
            block_to_blocktype("- valid unordered list\n- Second item\n- Third item"),
            BlockType.UNORDERED_LIST
        )
        self.assertNotEqual(
            block_to_blocktype("-invalid unordered list\n- Second item\n- Third item"),
            BlockType.UNORDERED_LIST
        )
        self.assertNotEqual(
            block_to_blocktype("- valid unordered list\n+ Second item\n- Third item"),
            BlockType.UNORDERED_LIST
        )