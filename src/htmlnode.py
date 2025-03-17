import unittest
from textnode import TextType
from textnode import TextNode

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode missing required tag")
        if self.children == None:
            raise ValueError("ParentNode missing required children")
        
        ending_tag = f"</{self.tag}>"
        opening_tag = f"<{self.tag}{self.props_to_html() if self.props else ''}>"
        html = ""
  
        for child in self.children:
            html += child.to_html()

        return opening_tag + html + ending_tag
    

def text_node_to_html_node(text_node):
    if text_node.text_type != TextType.NORMAL_TEXT and text_node.text_type != TextType.BOLD_TEXT and text_node.text_type != TextType.ITALIC_TEXT and text_node.text_type != TextType.CODE_TEXT and text_node.text_type != TextType.LINKS and text_node.text_type != TextType.IMAGES:
        raise Exception("Input type does not match")
    
    elif text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode(tag="b", value=text_node.text)
    
    elif text_node.text_type == TextType.NORMAL_TEXT:
        return LeafNode(tag=None, value=text_node.text)
    
    elif text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode(tag="i", value=text_node.text)
    
    elif text_node.text_type == TextType.CODE_TEXT:
        return LeafNode(tag="code", value=text_node.text)
    
    elif text_node.text_type == TextType.LINKS:
        return LeafNode(tag="a",value=text_node.text, props={"href": text_node.url})
    
    elif text_node.text_type == TextType.IMAGES:
        return LeafNode(tag="img",value="",props={"src": text_node.url, "alt": text_node.alt_text})

class tests(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()










            



                

                



