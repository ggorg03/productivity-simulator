import random

from .pile import TaskPile
from .task import Task
from .tasks_recorder import TasksRecorder


class Worker:
    def __init__(self,
                 speed: int = 1,
                 precision: float = 1):
        self.speed = speed
        self.precision = precision
        self.stage_id: int | None = None
        self.input_pile: TaskPile | None = None
        self.output_pile: TaskPile | None = None
        self.tasks_recorder = TasksRecorder()

    def step(self):
        for _ in range(self.speed):
            task = self.input_pile.get()
            if task is not None:
                self._work(task)
                self.output_pile.put_on_top(task)

    def _work(self, task: Task) -> None:
        task_outcome = task.get_outcome(self.stage_id)

        if task_outcome == Task.COMPLETED:
            return

        if task_outcome == Task.FAILED:
            self._remove_next_outcomes(task)

        task.set_outcome(self.stage_id, self._get_work_output())
        self.tasks_recorder.record(task)

    def _get_work_output(self):
        if random.random() < self.precision:
            return Task.COMPLETED
        else:
            return Task.FAILED

    def _remove_next_outcomes(self, task: Task):
        for stage_id in range(self.stage_id + 1, len(task.outcomes)):
            task.set_outcome(stage_id, None)