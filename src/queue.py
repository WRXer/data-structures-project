class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def __repr__(self):
        """
        Магический метод для отображения информации об объекте класса в режиме отладки
        """
        result = []
        if self.head is None:
            return ""
        head = self.head
        while head:
            result.append(head.data)
            head = head.next_node
        return '\n'.join(result)

    def __str__(self):
        """
        Магический метод для строкового представления объекта пользователю
        """
        result = []
        if self.head is None:
            return ""
        head = self.head
        while head:
            result.append(head.data)
            head = head.next_node
        return '\n'.join(result)

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        node.next_node = None
        if self.head == None:
            self.head = node    # если список пуст, то новый узел идет первым
            self.tail = self.head    # находим последний узел в списке
        else:
            self.tail.next_node = node    # добавляем новый узел
            self.tail.next_node.next_node = self.head
            self.tail = self.tail.next_node
            self.tail.next_node = None

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head == None:
            return None
        else:
            last_node = self.head
            self.head = self.head.next_node
        return last_node.data