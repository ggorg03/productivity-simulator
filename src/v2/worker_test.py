import random
import unittest
from unittest.mock import MagicMock

from .task import Task
from .worker import Worker


class WorkerTest(unittest.TestCase):
    def setUp(self) -> None:
        random.random = MagicMock(return_value=0.5)

    def test_work_sets_stage_state(self):
        worker = Worker(0, precision=1)

        task = Task()

        worker.work(task)

        self.assertEqual(task.get_state(0), Task.COMPLETED)

    def test_work_sets_multiple_stage_states(self):
        first_worker = Worker(0, precision=1)
        second_worker = Worker(1, precision=1)

        task = Task()

        first_worker.work(task)
        second_worker.work(task)

        self.assertEqual(task.get_state(0), Task.COMPLETED)
        self.assertEqual(task.get_state(1), Task.COMPLETED)

    def test_work_sets_failed_state(self):
        worker = Worker(0, precision=0.3)

        task = Task()

        worker.work(task)

        self.assertEqual(task.get_state(0), Task.FAILED)


if __name__ == '__main__':
    unittest.main()
