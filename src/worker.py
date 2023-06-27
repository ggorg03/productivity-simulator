import random as rd

from .task import Task
from .pilha_tarefas import PilhaTarefas


class Worker:
    def __init__(self,
                 speed: int = 3,
                 precision: float = None  # a number between 0 and 1
                 ):
        self.speed = speed
        self.precision = rd.random() if precision is None else precision
        self.task_pile = PilhaTarefas()

    def execute_task(self, task: Task) -> Task:
        task.tries += 1

        if task.difficulty <= self.precision:
            task.is_completed = True
        else:
            task.reset_difficulty()

        return task

    def get_new_tasks(self, task_count: int) -> None:
        self.task_pile.gerar_novas_tarefas(task_count)

    def work(self, task_count: int = 5) -> list[Task]:
        tasks = self.task_pile.pegar_tarefas(self.speed)
        tasks = [self.execute_task(task) for task in tasks]

        completed_tasks = [task for task in tasks if task.is_completed]
        failed_tasks = [task for task in tasks if not task.is_completed]

        self.task_pile.adicionar_tarefas(failed_tasks)

        return completed_tasks

    def __eq__(self, obj) -> bool:
        return isinstance(obj, Worker) and \
            self.speed == obj.speed and \
            self.precision == obj.precision and \
            self.task_pile == obj.task_pile

    def __str__(self) -> str:
        return str(self.task_pile)
