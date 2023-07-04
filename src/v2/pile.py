import collections

from .task import Task


class TaskPile:
    def __init__(self):
        self.tasks = collections.deque()

    def put(self, task: Task) -> None:
        self.tasks.append(task)

    def get(self) -> Task | None:
        try:
            return self.tasks.popleft()
        except IndexError:
            return None
