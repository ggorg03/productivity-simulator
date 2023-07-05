from .pipeline import Pipeline


class Simulation:
    def __init__(self, pipeline: Pipeline):
        self.pipeline = pipeline

    def run(self, step_count: int):
        for i in range(step_count):
            self.pipeline.step()

        print(f"Result: {self.pipeline.success_count()} of {len(self.pipeline.tasks)} tasks completed")
        print("Tries:")
        for task in self.pipeline.tasks:
            print(task.tries)
