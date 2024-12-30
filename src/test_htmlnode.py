import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
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

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_props(self):
        node = LeafNode(tag="a", value="Click here", props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.example.com" target="_blank">Click here</a>')

    def test_to_html_with_tag_no_props(self):
        node = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph.</p>')

    def test_to_html_without_tag(self):
        node = LeafNode(tag=None, value="Just some text.")
        self.assertEqual(node.to_html(), "Just some text.")

    def test_to_html_raises_value_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="span", value=None)


if __name__ == "__main__":
    unittest.main()