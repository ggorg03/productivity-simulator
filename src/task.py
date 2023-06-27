import random as rd


class Task:
    id = 0

    def __init__(self, difficulty: float = None, tries: int = 0):
        self.id = Task.id
        self.difficulty = rd.random() if difficulty is None else difficulty
        self.tries = tries
        self.is_completed = False

        Task.id += 1

    def increment_tries(self) -> None:
        self.tries += 1

    def reset_difficulty(self) -> None:
        self.difficulty = rd.random()

    def __str__(self):
        return str(self.difficulty)

    def __eq__(self, obj) -> bool:
        return isinstance(obj, Task) and \
            self.difficulty == obj.difficulty and \
            self.is_completed == obj.is_completed and \
            self.tries == obj.tries
