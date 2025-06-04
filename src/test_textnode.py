import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.CODE_TEXT)
        self.assertNotEqual(node1,node2)
    def test_url_none(self):
        node1 = TextNode("This is a text node", TextType.BOLD_TEXT, url=None)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, url=None)
        self.assertEqual(node1,node2)
    def test_url_diff(self):
        node1 = TextNode("This is a text node", TextType.BOLD_TEXT, url="bing.com")
        node2= TextNode("This is a text node", TextType.BOLD_TEXT, url="google.com")
        self.assertNotEqual(node1,node2)
    def test_url_one_none(self):
        node1 = TextNode("This is a text node", TextType.BOLD_TEXT, url=None)
        node2= TextNode("This is a text node", TextType.BOLD_TEXT, url="google.com")
        self.assertNotEqual(node1,node2)
    def test_text(self):
        node1 = TextNode("This is 2 text nodes", TextType.BOLD_TEXT, url=None)
        node2= TextNode("This is a text node", TextType.BOLD_TEXT, url=None)
        self.assertNotEqual(node1,node2)

if __name__ == "__main__":
    unittest.main()