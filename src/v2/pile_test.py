import unittest

from .task import Task
from .pile import TaskPile


class TaskPileTest(unittest.TestCase):
    def test_put_then_get(self):
        pile = TaskPile()
        task = Task()

        pile.put(task)

        self.assertEqual(pile.get(), task)

    def test_get_empty(self):
        pile = TaskPile()

        self.assertEqual(pile.get(), None)

    def test_get_two_different_tasks(self):
        pile = TaskPile()
        task1 = Task()
        task2 = Task()

        pile.put(task1)
        pile.put(task2)

        self.assertEqual(pile.get(), task1)
        self.assertEqual(pile.get(), task2)

    def test_put_many(self):
        pile = TaskPile()
        task1 = Task()
        task2 = Task()

        pile.put(task1, task2)

        self.assertEqual(pile.get(), task1)
        self.assertEqual(pile.get(), task2)


if __name__ == '__main__':
    unittest.main()
