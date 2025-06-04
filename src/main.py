from textnode import TextNode
from textnode import TextType
print("Hello World!")

type = "bold"
text = TextType.BOLD_TEXT
link = "google.com"

def main():
 test = TextNode(type,text,link)
 print(test)


main()