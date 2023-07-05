import collections

from .task import Task


class TaskPile:
    def __init__(self):
        self.tasks = collections.deque()

    def put(self, *tasks: Task) -> None:
        self.tasks.extend(tasks)

    def get(self) -> Task | None:
        try:
            return self.tasks.popleft()
        except IndexError:
            return None

    def __len__(self) -> int:
        return len(self.tasks)
