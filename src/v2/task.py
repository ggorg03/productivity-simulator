class Task:
    FAILED = "Failed"
    COMPLETED = "Completed"

    def __init__(self, num_stages: int = 2):
        self.tries = 0
        self.outcomes = [None for _ in range(num_stages)]

    def set_outcome(self, stage_id, state):
        self.outcomes[stage_id] = state

    def get_outcome(self, stage_id):
        return self.outcomes[stage_id]

    def has_outcome(self, stage_id):
        return self.outcomes[stage_id] is not None

    def fully_complete(self) -> bool:
        for outcome in self.outcomes:
            if outcome != Task.COMPLETED:
                return False
        return True

    def __repr__(self):
        return f"<Task #{id(self)} {str(self.outcomes)}>"
