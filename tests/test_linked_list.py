"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    """
        Класс для тестирования класса LinkedList
        """
    def test_init(self):
        """
        Тест для инита
        """
        ll = LinkedList()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_insert_beginning(self):
        """
        Тест для добавления элемента в начало связанного списка
        """
        ll = LinkedList()
        self.assertIsNone(ll.head)
        ll.insert_beginning("test")
        self.assertEqual(ll.head.data, "test")
        ll.insert_beginning("test2")
        self.assertEqual(ll.head.data, "test2")

    def test_insert_at_end(self):
        """
        Тест для добавления элемента в начало связанного списка
        """
        ll = LinkedList()
        self.assertIsNone(ll.head)
        ll.insert_at_end("test")
        self.assertEqual(ll.tail.data, "test")
        ll.insert_at_end("test2")
        self.assertEqual(ll.tail.data, "test2")

    def test_str(self):
        """
        Тест __str__
        """
        ll = LinkedList()
        self.assertEqual(str(ll), "None")
        ll.insert_beginning("test")
        self.assertEqual(str(ll), "test -> None")
        ll.insert_beginning("test2")
        self.assertEqual(str(ll), "test2 -> test -> None")

    def test_to_list(self):
        """
        Тест to_list
        """
        ll = LinkedList()
        self.assertEqual(type(ll.to_list()), list)
        ll.insert_beginning("test")
        ll.insert_beginning("test2")
        self.assertEqual(ll.to_list(), ["test2", "test"])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'test'})
        ll.insert_at_end({'id': 2, 'username': 'test2'})
        self.assertEqual(ll.get_data_by_id(1), {'id': 1, 'username': 'test'})

    def test_get_data_by_id_type_error(self):
        ll = LinkedList()
        ll.insert_beginning("testt")
        self.assertIsNone(ll.get_data_by_id(10))
