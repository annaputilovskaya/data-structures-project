from src.node import Node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        """
        Отображение информации об объекте класса пользователю


        :return: "<data3>\n<data2>\n<data1>"
        """
        string = ''
        top = self.top
        while top is not None:
            string += f'{top.data}\n'
            top = top.next_node
        return string.rstrip()

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека


        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения


        :return: данные удаленного элемента
        """
        top_node = self.top
        self.top = top_node.next_node
        return top_node.data
