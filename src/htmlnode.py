

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children={len(self.children)}, props={self.props})"
    
    def LeafNode(HTMLNode):
        def __init__(self, tag, value, props=None):
            if value is None:
                raise ValueError("All leaf nodes must have a value.")
            
            super().__init__(tag=tag, value=value, children=None, props=props)
            self.children = []

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


