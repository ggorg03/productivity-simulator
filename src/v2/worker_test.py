import random
import unittest
from unittest.mock import MagicMock

from .pile import TaskPile
from .task import Task
from .worker import Worker


class WorkerTest(unittest.TestCase):
    def setUp(self) -> None:
        random.random = MagicMock(return_value=0.5)

    def test_step_moves_tasks_between_piles(self):
        input_pile = TaskPile()
        output_pile = TaskPile()
        task = Task()

        input_pile.put(task)

        worker = Worker()
        worker.stage_id = 0
        worker.input_pile = input_pile
        worker.output_pile = output_pile

        worker.step()

        self.assertEqual(input_pile.get(), None)
        self.assertEqual(output_pile.get(), task)

    def test_step_can_complete_task(self):
        input_pile = TaskPile()
        output_pile = TaskPile()
        task = Task()

        input_pile.put(task)

        worker = Worker(precision=1)
        worker.stage_id = 0
        worker.input_pile = input_pile
        worker.output_pile = output_pile

        worker.step()

        updated_task = output_pile.get()
        self.assertEqual(updated_task.get_outcome(0), Task.COMPLETED)

    def test_step_can_fail_task(self):
        input_pile = TaskPile()
        output_pile = TaskPile()
        task = Task()

        input_pile.put(task)

        worker = Worker(precision=0)
        worker.stage_id = 0
        worker.input_pile = input_pile
        worker.output_pile = output_pile

        worker.step()

        updated_task = output_pile.get()
        self.assertEqual(updated_task.get_outcome(0), Task.FAILED)

    def test_step_multiple_times_same_worker(self):
        input_pile = TaskPile()
        output_pile = TaskPile()

        input_pile.put(Task())
        input_pile.put(Task())

        worker = Worker(precision=1)
        worker.stage_id = 0
        worker.input_pile = input_pile
        worker.output_pile = output_pile

        worker.step()
        worker.step()

        updated_task1 = output_pile.get()
        updated_task2 = output_pile.get()

        self.assertEqual(updated_task1.get_outcome(0), Task.COMPLETED)
        self.assertEqual(updated_task2.get_outcome(0), Task.COMPLETED)

    def test_step_multiple_workers(self):
        input_pile = TaskPile()
        transport_pile = TaskPile()
        output_pile = TaskPile()

        input_pile.put(Task())

        worker1 = Worker(precision=1)
        worker1.stage_id = 0
        worker1.input_pile = input_pile
        worker1.output_pile = transport_pile

        worker2 = Worker(precision=1)
        worker2.stage_id = 1
        worker2.input_pile = transport_pile
        worker2.output_pile = output_pile

        worker1.step()
        worker2.step()

        task = output_pile.get()

        self.assertEqual(task.get_outcome(0), Task.COMPLETED)
        self.assertEqual(task.get_outcome(1), Task.COMPLETED)


if __name__ == '__main__':
    unittest.main()
