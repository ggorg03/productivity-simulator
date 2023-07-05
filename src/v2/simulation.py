from .pile import TaskPile
from .task import Task
from .worker import Worker


class Simulation:
    def __init__(self):
        self.piles = [
            TaskPile(),
            TaskPile(),
            TaskPile()
        ]

        self.workers = [
            Worker(0, precision=0.5, input_pile=self.piles[0], output_pile=self.piles[1]),
            Worker(1, precision=0.5, input_pile=self.piles[1], output_pile=self.piles[2])
        ]

        self.piles[0].put(*[Task() for _ in range(10)])

    def run(self):
        for i in range(8):
            for worker in self.workers:
                worker.step()

        for task in self.piles[2]:
            print(task)
