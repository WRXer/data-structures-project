"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    """
    Класс для тестирования класса Stack
    """
    def test_init(self):
        """
        Тест для инита
        """
        stack = Stack()
        self.assertIsNone(stack.top)

    def test_push(self):
        """
        Тест для добавления элемента
        """
        stack = Stack()
        self.assertIsNone(stack.top)
        stack.push("test")
        self.assertEqual(stack.top.data, "test")

    def test_pop(self):
        """
        Тест для удаления верхнего элемента
        """
        stack = Stack()
        stack.push("test")
        stack.push("test2")
        self.assertEqual(stack.top.data, "test2")
        stack.pop()
        self.assertEqual(stack.pop(), "test")