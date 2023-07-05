from .pipeline import Pipeline
from .stage import Stage
from .task import Task


class Simulation:
    def __init__(self):
        self.pipeline = Pipeline([
            Stage(num_workers=1, precision_distribution=lambda: 0.5),
            Stage(num_workers=1, precision_distribution=lambda: 0.5),
        ])

        self.pipeline.add_tasks(10)

    def run(self, step_count: int):
        for i in range(step_count):
            self.pipeline.step()

        print(self.pipeline.sentinel.success_count)
