from .pile import TaskPile
from .sentinel import Sentinel
from .stage import Stage
from .task import Task


class Pipeline:
    def __init__(self, stages: list[Stage]):
        piles = [TaskPile() for _ in range(len(stages) + 1)]

        for i in range(len(stages)):
            stages[i].set_stage_id(i)
            stages[i].set_input_pile(piles[i])
            stages[i].set_output_pile(piles[i + 1])

        self.stages = stages
        self.input_pile = piles[0]
        self.output_pile = piles[-1]
        self.success_pile = TaskPile()

        self.sentinel = Sentinel(
            result_pile=self.output_pile,
            success_pile=self.success_pile,
            failed_pile=self.input_pile
        )

    def add_tasks(self, num_tasks: int):
        self.input_pile.put(*[Task(len(self.stages)) for _ in range(num_tasks)])

    def step(self):
        for stage in self.stages:
            stage.step()

        self.sentinel.step()
