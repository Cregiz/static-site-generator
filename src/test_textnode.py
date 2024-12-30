import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_same_properties(self):
        node1 = TextNode("This is a text node", TextType.PLAIN, "https://example.com")
        node2 = TextNode("This is a text node", TextType.PLAIN, "https://example.com")
        self.assertEqual(node1, node2)

    def test_eq_different_text(self):
        node1 = TextNode("Text A", TextType.PLAIN, "https://example.com")
        node2 = TextNode("Text B", TextType.PLAIN, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_eq_different_text_type(self):
        node1 = TextNode("This is a text node", TextType.PLAIN, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_eq_different_url(self):
        node1 = TextNode("This is a text node", TextType.PLAIN, "https://example1.com")
        node2 = TextNode("This is a text node", TextType.PLAIN, "https://example2.com")
        self.assertNotEqual(node1, node2)

    def test_eq_url_none(self):
        node1 = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a text node", TextType.PLAIN, None)
        self.assertEqual(node1, node2)



if __name__ == "__main__":
    unittest.main()
