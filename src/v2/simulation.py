from .task import Task
from .worker import Worker


class Simulation:
    def __init(self):
        self.workers = [
            Worker(0, 0.5),
            Worker(1, 0.5)
        ]

        self.tasks = [
            Task(),
            Task()
        ]

    def run(self):
        for task in self.tasks:
            self._process_task(task)

        print(self.tasks)

    def _process_task(self, task):
        for worker in self.workers:
            worker.work(task)
