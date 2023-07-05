import unittest

from .task import Task
from .pile import TaskPile
from .stage import Stage


class StageTest(unittest.TestCase):
    def test_step_moves_task_between_piles(self):
        input_pile = TaskPile()
        output_pile = TaskPile()
        task = Task()

        input_pile.put(task)

        stage = Stage(
            stage_id=0,
            num_workers=1,
            precision_distribution=lambda: 0.5)

        stage.set_input_pile(input_pile)
        stage.set_output_pile(output_pile)

        stage.step()

        self.assertEqual(output_pile.get(), task)


if __name__ == '__main__':
    unittest.main()
