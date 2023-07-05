import random

from .pile import TaskPile
from .stage import Stage
from .task import Task


class Simulation:
    def __init__(self):
        self.piles = [
            TaskPile(),
            TaskPile(),
            TaskPile()
        ]

        self.stages = [
            Stage(stage_id=0,
                  num_workers=1,
                  precision_distribution=lambda: 0.5),
            Stage(stage_id=1,
                  num_workers=1,
                  precision_distribution=lambda: 0.5),
        ]

        for i in range(len(self.stages)):
            self.stages[i].set_input_pile(self.piles[i])
            self.stages[i].set_output_pile(self.piles[i+1])

        self.piles[0].put(*[Task() for _ in range(10)])

    def run(self):
        for i in range(8):
            for stage in self.stages:
                stage.step()

        for task in self.piles[2]:
            print(task)
