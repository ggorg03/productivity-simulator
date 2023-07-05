from typing import Callable

from .pile import TaskPile
from .worker import Worker


class Stage:
    def __init__(self,
                 num_workers: int,
                 precision_distribution: Callable[[], float]):
        self.workers = [Worker(precision=precision_distribution()) for _ in range(num_workers)]

    def set_stage_id(self, stage_id: int) -> None:
        for worker in self.workers:
            worker.stage_id = stage_id

    def set_input_pile(self, input_pile: TaskPile) -> None:
        for worker in self.workers:
            worker.input_pile = input_pile

    def set_output_pile(self, output_pile: TaskPile) -> None:
        for worker in self.workers:
            worker.output_pile = output_pile

    def step(self):
        for worker in self.workers:
            worker.step()
