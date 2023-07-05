import random

from .pile import TaskPile
from .task import Task


class Worker:
    def __init__(self,
                 stage_id,
                 precision: float = 1,
                 input_pile: TaskPile = TaskPile(),
                 output_pile: TaskPile = TaskPile()):
        self.stage_id = stage_id
        self.precision = precision
        self.input_pile = input_pile
        self.output_pile = output_pile

    def step(self):
        task = self.input_pile.get()
        self._work(task)
        self.output_pile.put(task)

    def _work(self, task: Task) -> None:
        task.set_state(self.stage_id, self._get_work_output())

    def _get_work_output(self):
        if random.random() < self.precision:
            return Task.COMPLETED
        else:
            return Task.FAILED
