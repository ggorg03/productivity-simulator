from typing import Callable

from .pile import TaskPile
from .worker import Worker


class Stage:
    def __init__(self,
                 stage_id: int,
                 num_workers: int,
                 precision_distribution: Callable[[], float]):
        self.workers = [
            Worker(
                stage_id,
                precision=precision_distribution(),
            ) for _ in range(num_workers)
        ]

    def set_input_pile(self, input_pile):
        for worker in self.workers:
            worker.input_pile = input_pile

    def set_output_pile(self, output_pile):
        for worker in self.workers:
            worker.output_pile = output_pile

    def step(self):
        for worker in self.workers:
            worker.step()
