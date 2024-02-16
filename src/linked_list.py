from src.node import Node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        """
        Создает экземпляр класса LinkedList
        """
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()

    def to_list(self) -> list:
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""
        ll_list = []
        node = self.head
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, data_id: int) -> dict:
        """
        Возвращает первый найденный в LinkedList словарь с ключом 'id',
        значение которого равно переданному в метод значению
        """
        l_list = self.to_list()
        if len(l_list) > 0:
            for dictionary in l_list:
                try:
                    if dictionary['id'] == data_id:
                        return dictionary
                except TypeError:
                    print('Данные не являются словарем или в словаре нет id')
