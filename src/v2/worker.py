import random

from .pile import TaskPile
from .task import Task


class Worker:
    def __init__(self,
                 precision: float = 1):
        self.precision = precision
        self.stage_id: int | None = None
        self.input_pile: TaskPile | None = None
        self.output_pile: TaskPile | None = None

    def step(self):
        task = self.input_pile.get()
        if task:
            self._work(task)
            self.output_pile.put(task)

    def _work(self, task: Task) -> None:
        task_outcome = task.get_outcome(self.stage_id)

        if task_outcome == Task.COMPLETED:
            return

        if task_outcome == Task.FAILED:
            self._remove_next_outcomes(task)

        task.set_outcome(self.stage_id, self._get_work_output())

    def _get_work_output(self):
        if random.random() < self.precision:
            return Task.COMPLETED
        else:
            return Task.FAILED

    def _remove_next_outcomes(self, task: Task):
        for stage_id in range(self.stage_id + 1, len(task.outcomes)):
            task.set_outcome(stage_id, None)