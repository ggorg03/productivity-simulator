from .pile import TaskPile


class Sentinel:
    def __init__(self, result_pile: TaskPile, failed_pile: TaskPile):
        self.result_pile = result_pile
        self.failed_pile = failed_pile
        self.success_count = 0

    def step(self):
        while True:
            task = self.result_pile.get()

            if task is None:
                break

            if task.fully_complete():
                self.success_count += 1
            else:
                self.failed_pile.put(task)
