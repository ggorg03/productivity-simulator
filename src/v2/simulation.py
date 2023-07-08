from .tasks_recorder import TasksRecorder
from .pipeline import Pipeline


class Simulation():
    def __init__(self, id: int, pipeline: Pipeline):
        self.id = id
        self.pipeline = pipeline
        self.tasks_recorder = TasksRecorder()

    def run(self, step_count: int):
        for step in range(step_count):
            self.tasks_recorder.set_context(self.id, step)
            self.pipeline.step()

        return self.pipeline.success_count()