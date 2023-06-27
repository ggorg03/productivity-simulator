import random as rd

from .task import Task


class Pile:
    id = 0

    def __init__(self):
        self.id = Pile.id
        self.tasks = []

        # increment id register
        Pile.id += 1

    def size(self):
        return len(self.tasks)

    def generate_new_tasks(self, quantity: int = 1) -> None:
        self.tasks += [Task(rd.random()) for task in range(quantity)]

    def add_tasks(self, tasks: list, append: bool = True) -> None:
        if not append:
            self.tasks = self.tasks + tasks
        else:
            self.tasks = tasks + self.tasks

    def get_tasks(self, quantity: int = 1) -> list:
        tasks = self.tasks[:quantity]
        self.tasks = self.tasks[quantity:]

        return tasks

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Pile):
            return False

        if self.size() != obj.size():
            return False

        for t in self.tasks:
            if t not in obj.tasks:
                return False

        return True

    def __str__(self) -> str:
        return str(self.tasks)
