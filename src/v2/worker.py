import random

from .task import Task


class Worker:
    def __init__(self, stage_id, precision: float):
        self.stage_id = stage_id
        self.precision = precision

    def work(self, task: Task) -> None:
        task.set_stage_state(self.stage_id, self._get_work_output())

    def _get_work_output(self):
        if random.random() < self.precision:
            return Task.COMPLETED
        else:
            return Task.FAILED
