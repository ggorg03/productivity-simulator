from .pipeline import Pipeline


class Simulation:
    def __init__(self, pipeline: Pipeline):
        self.pipeline = pipeline

    def run(self, step_count: int):
        for i in range(step_count):
            self.pipeline.step()

        print(len(self.pipeline.success_pile))
