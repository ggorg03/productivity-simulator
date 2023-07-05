import random

from .pile import TaskPile
from .task import Task


class Worker:
    def __init__(self,
                 stage_id: int,
                 precision: float = 1):
        self.stage_id = stage_id
        self.precision = precision
        self.input_pile: TaskPile | None = None
        self.output_pile: TaskPile | None = None

    def step(self):
        task = self.input_pile.get()
        if task:
            self._work(task)
            self.output_pile.put(task)

    def _work(self, task: Task) -> None:
        task.set_state(self.stage_id, self._get_work_output())

    def _get_work_output(self):
        if random.random() < self.precision:
            return Task.COMPLETED
        else:
            return Task.FAILED
