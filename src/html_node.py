test_prop = {
    "href": "https://www.google.com",
    "target": "_blank",
}
result = ""

class HTMLNode():
    def __init__(self, tag = None, value = None, props = None, children= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props == None:
            return ""
        else:
            for key, value in self.props.items():
                result += f' {key}="{value}"'
                
            return result
        
        # return (f' href="{self.props["href"]}" target="{self.props["target"]}"')
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props, children=None)
        
        
        
    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"



def main():
    # Test the props_to_html method directly
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
    print("Props:", node.props)
    print("Props to HTML:", repr(node.props_to_html()))
    print("Full HTML:", node.to_html())

main()