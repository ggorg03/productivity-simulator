import unittest

from .task import Task
from .worker import Worker


class WorkerTest(unittest.TestCase):
    def test_work_sets_stage_state(self):
        worker = Worker(0)

        task = Task()

        worker.work(task)

        self.assertEqual(task.get_stage_state(0), Task.COMPLETED)

    def test_work_sets_multiple_stage_states(self):
        first_worker = Worker(0)
        second_worker = Worker(1)

        task = Task()

        first_worker.work(task)
        second_worker.work(task)

        self.assertEqual(task.get_stage_state(0), Task.COMPLETED)
        self.assertEqual(task.get_stage_state(1), Task.COMPLETED)


if __name__ == '__main__':
    unittest.main()
