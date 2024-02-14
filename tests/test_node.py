import unittest

from src.node import Node


class TestNode(unittest.TestCase):
    def test_initial_node(self):
        node1 = Node(5, Node)
        node2 = Node('a', node1)
        self.assertEqual(node1.data, 5)
        self.assertEqual(node2.next_node, node1)