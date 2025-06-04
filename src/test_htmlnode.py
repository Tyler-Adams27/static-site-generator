from html_node import HTMLNode
from html_node import LeafNode
import unittest


test_prop = {
    "href": "https://www.google.com",
    "target": "_blank",
}
expected_output = ' href="https://www.google.com" target="_blank"'
empty = ""

class test_html_node(unittest.TestCase):
    
    def test_output_correct(self):
        node = HTMLNode(None,None,test_prop,None)
        output = node.props_to_html()
        self.assertEqual(output,expected_output)
    
    def test_output_none(self):
        node = HTMLNode(None,None,None,None)
        output = node.props_to_html()
        self.assertEqual(output,empty)
    
    def test_empty_dict(self):
        node = HTMLNode(None,None,None,{})
        output = node.props_to_html()
        self.assertEqual(output,empty)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


            
    

if __name__ == "__main__":
    unittest.main()