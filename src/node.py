class Node:
    """Класс для узла"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node


        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node
