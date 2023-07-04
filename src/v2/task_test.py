import unittest

from .task import Task


class TaskTest(unittest.TestCase):

    def setUp(self) -> None:
        self.task = Task()

    def test_set_single_stage_state(self):
        self.task.set_state(0, Task.COMPLETED)

        self.assertEqual(self.task.get_state(0), Task.COMPLETED)

    def test_set_multiple_stage_state(self):
        self.task.set_state(0, Task.FAILED)
        self.task.set_state(1, Task.COMPLETED)

        self.assertEqual(self.task.get_state(0), Task.FAILED)
        self.assertEqual(self.task.get_state(1), Task.COMPLETED)


if __name__ == '__main__':
    unittest.main()
