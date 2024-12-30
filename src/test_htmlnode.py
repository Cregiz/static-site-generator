import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html_with_attributes(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_without_attributes(self):
        node = HTMLNode(tag="div")
        self.assertEqual(node.props_to_html(), "")

    def test_nested_nodes(self):
        child_node = HTMLNode(tag="span", value="Hello")
        parent_node = HTMLNode(tag="div", children=[child_node])
        self.assertEqual(parent_node.tag, "div")
        self.assertEqual(len(parent_node.children), 1)
        self.assertEqual(parent_node.children[0].tag, "span")
        self.assertEqual(parent_node.children[0].value, "Hello")

if __name__ == "__main__":
    unittest.main()