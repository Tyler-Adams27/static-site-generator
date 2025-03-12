from enum import Enum

test_text = "Hello World"
test_link = "link"
test_url = "https://www.google.com"

class TextType(Enum):
    normal_text = "normal"
    text_bold = "bold"
    text_italic = "italic"
    text_code = "code"
    text_link = "link"
    text_image = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        text_type_value = self.text_type.value if hasattr(self.text_type, 'value') else self.text_type
        return f"TextNode({self.text}, {text_type_value}, {self.url})"


def main():
    print(TextNode(test_text,test_link,test_url))
        

main()

