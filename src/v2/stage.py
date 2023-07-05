from typing import Callable

from .pile import TaskPile
from .worker import Worker


class Stage:
    def __init__(self,
                 stage_id: int,
                 num_workers: int,
                 precision_distribution: Callable[[], float],
                 input_pile: TaskPile,
                 output_pile: TaskPile):
        self.input_pile = input_pile
        self.output_pile = output_pile

        self.workers = [
            Worker(
                stage_id,
                precision=precision_distribution(),
                input_pile=input_pile,
                output_pile=self.output_pile
            ) for _ in range(num_workers)
        ]

    def step(self):
        for worker in self.workers:
            worker.step()
