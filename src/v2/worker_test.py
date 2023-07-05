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

        worker = Worker(0, input_pile=input_pile, output_pile=output_pile)

        worker.step()

        self.assertEqual(input_pile.get(), None)
        self.assertEqual(output_pile.get(), task)

    def test_step_can_complete_task(self):
        input_pile = TaskPile()
        output_pile = TaskPile()
        task = Task()

        input_pile.put(task)

        worker = Worker(0, precision=1, input_pile=input_pile, output_pile=output_pile)

        worker.step()

        updated_task = output_pile.get()
        self.assertEqual(updated_task.get_state(0), Task.COMPLETED)

    def test_step_can_fail_task(self):
        input_pile = TaskPile()
        output_pile = TaskPile()
        task = Task()

        input_pile.put(task)

        worker = Worker(0, precision=0, input_pile=input_pile, output_pile=output_pile)

        worker.step()

        updated_task = output_pile.get()
        self.assertEqual(updated_task.get_state(0), Task.FAILED)

    def test_step_multiple_times_same_worker(self):
        input_pile = TaskPile()
        output_pile = TaskPile()

        input_pile.put(Task())
        input_pile.put(Task())

        worker = Worker(0, precision=1, input_pile=input_pile, output_pile=output_pile)

        worker.step()
        worker.step()

        updated_task1 = output_pile.get()
        updated_task2 = output_pile.get()

        self.assertEqual(updated_task1.get_state(0), Task.COMPLETED)
        self.assertEqual(updated_task2.get_state(0), Task.COMPLETED)

    def test_step_multiple_workers(self):
        input_pile = TaskPile()
        transport_pile = TaskPile()
        output_pile = TaskPile()

        input_pile.put(Task())

        worker1 = Worker(0, precision=1, input_pile=input_pile, output_pile=transport_pile)
        worker2 = Worker(1, precision=1, input_pile=transport_pile, output_pile=output_pile)

        worker1.step()
        worker2.step()

        task = output_pile.get()

        self.assertEqual(task.get_state(0), Task.COMPLETED)
        self.assertEqual(task.get_state(1), Task.COMPLETED)


if __name__ == '__main__':
    unittest.main()
