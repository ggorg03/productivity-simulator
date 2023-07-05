from .pile import TaskPile
from .stage import Stage


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

    def step(self):
        for stage in self.stages:
            stage.step()