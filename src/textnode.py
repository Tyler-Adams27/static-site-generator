from enum import Enum


class TextType(Enum):
    NORMAL_TEXT = "text"
    BOLD_TEXT = "bold"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGES_TEXT = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self):
        return self.text == self.text and self.text_type == self.text_type and self.url == self.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def main():
    text_node = TextNode("This is a test", TextType.LINK_TEXT, "google.com")
    print(text_node)

if __name__ == "__main__":
    main()