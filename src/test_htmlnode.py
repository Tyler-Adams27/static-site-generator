import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode("a", "Link text", None, {"href": "https://example.com", "target": "_blank"})
        expected = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
    
    def test_props_to_html_without_props(self):
        node = HTMLNode("p", "Paragraph text")
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_empty_props(self):
        node = HTMLNode("div", "Content", None, {})
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()
        