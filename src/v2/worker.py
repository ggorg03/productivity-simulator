from .task import Task


class Worker:
    def __init__(self, stage_id):
        self.stage_id = stage_id

    def work(self, task: Task) -> None:
        task.set_stage_state(self.stage_id, Task.COMPLETED)
