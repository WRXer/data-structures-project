"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):
    """
    Класс для тестирования класса Stack
    """
    def test_init(self):
        """
        Тест для инита
        """
        queue = Queue()
        self.assertIsNone(queue.head)

    def test_str(self):
        """
        Тест __str__
        """
        queue = Queue()
        assert str(queue) == ""
        queue.enqueue("test")
        assert str(queue) == "test"

    def test_repr(self):
        """
        Тест для __repr__
        """
        queue = Queue()
        assert str(queue) == ""
        queue.enqueue("test")
        assert repr(queue) == "test"

    def test_enqueue(self):
        """
        Тест для добавления элемента
        """
        queue = Queue()
        self.assertIsNone(queue.head)
        queue.enqueue("test")
        self.assertEqual(queue.head.data, "test")

    def test_dequeue(self):
        queue = Queue()
        self.assertEqual(queue.head, None)
        queue.enqueue("test")
        queue.enqueue("test2")
        self.assertEqual(queue.head.data, "test")
        queue.dequeue()
        self.assertNotEqual(queue.head.data, "test")
