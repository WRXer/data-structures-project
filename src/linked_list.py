class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        """Конструктор класса"""
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data, None)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            node.next_node = self.head
            self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data, None)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next_node = node
            self.tail = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        counter = 0
        ll_string = ''
        while node:
            if counter == 0:
                ll_string += f'{str(node.data)} ->'
                node = node.next_node
                counter += 1
            else:
                ll_string += f' {str(node.data)} ->'
                node = node.next_node

        ll_string += ' None'
        return ll_string

    def to_list(self):
        """
        Функция возвращает список с данными, содержащимися в односвязном списке `LinkedList`
        """
        list = []
        node = self.head
        while node:
            list.append(node.data)
            node = node.next_node
        return list

    def get_data_by_id(self, id):
        """
        Функция возвращает первый найденный в `LinkedList` словарь с ключом 'id', значение которого равно переданному в метод значению.
        """
        lst = self.to_list()
        for item in lst:
            try:
                if item['id'] == id:
                    return item
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")
        return None