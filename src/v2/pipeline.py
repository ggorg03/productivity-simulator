from .pile import TaskPile
from .sentinel import Sentinel
from .stage import Stage
from .task import Task


class Pipeline:
    def __init__(self, stages: list[Stage], num_tasks: int):
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

        self.tasks = [Task(task_id=i + 1, num_stages=len(self.stages)) for i in range(num_tasks)]
        self.input_pile.put(*self.tasks)

    def step(self):
        for stage in self.stages:
            stage.step()

        self.sentinel.step()

    def success_count(self):
        count = 0
        for task in self.tasks:
            if task.fully_complete():
                count += 1
        return count
