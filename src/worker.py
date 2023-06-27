import random as rd

from .task import Task
from .pile import Pile


class Worker:
    def __init__(self, speed: int, precision: float):
        self.speed = speed
        self.precision = precision
        self.task_pile = Pile()

    def execute_task(self, task: Task) -> Task:
        task.tries += 1

        if task.difficulty <= self.precision:
            task.is_completed = True
        else:
            task.reset_difficulty()

        return task

    def get_new_tasks(self, task_count: int) -> None:
        self.task_pile.generate_new_tasks(task_count)

    def work(self) -> list[Task]:
        tasks = self.task_pile.get_tasks(self.speed)
        tasks = [self.execute_task(task) for task in tasks]

        completed_tasks = [task for task in tasks if task.is_completed]
        failed_tasks = [task for task in tasks if not task.is_completed]

        self.task_pile.add_tasks(failed_tasks)

        return completed_tasks

    def __eq__(self, obj) -> bool:
        return isinstance(obj, Worker) and \
            self.speed == obj.speed and \
            self.precision == obj.precision and \
            self.task_pile == obj.task_pile

    def __str__(self) -> str:
        return str(self.task_pile)
