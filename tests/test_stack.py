import unittest


from src.stack import Node, Stack


class TestNode(unittest.TestCase):
    def test_initial_node(self):
        node1 = Node(5, Node)
        node2 = Node('a', node1)
        self.assertEqual(node1.data, 5)
        self.assertEqual(node2.next_node, node1)


class TestStack(unittest.TestCase):
    def test_push(self):
        stack1 = Stack()
        stack1.push('test1')
        self.assertEqual(stack1.top.data, 'test1')
        stack1.push('test2')
        self.assertEqual(stack1.top.data, 'test2')

    def test_pop(self):
        stack2 = Stack()
        stack2.push('test3')
        stack2.push('test4')
        data1 = stack2.pop()
        self.assertEqual(data1, 'test4')
        self.assertEqual(stack2.top.data, 'test3')
        data2 = stack2.pop()
        self.assertEqual(data2, 'test3')
        self.assertEqual(stack2.top, None)

    def test_str(self):
        stack3 = Stack()
        self.assertEqual(str(stack3), '')
        stack3.push('test5')
        stack3.push('test6')
        stack3.push('test7')
        self.assertEqual(str(stack3), 'test7\ntest6\ntest5')
