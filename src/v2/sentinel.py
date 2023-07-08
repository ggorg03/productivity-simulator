from .pile import TaskPile


class Sentinel:
    def __init__(self, result_pile: TaskPile, success_pile: TaskPile, failed_pile: TaskPile):
        self.result_pile = result_pile
        self.success_pile = success_pile
        self.failed_pile = failed_pile

    def step(self):
        while True:
            task = self.result_pile.get()

            if task is None:
                break

            task.tries += 1

            if task.fully_complete():
                self.success_pile.put(task)
                task.set_out_pipeline()
            else:
                self.failed_pile.put(task)
