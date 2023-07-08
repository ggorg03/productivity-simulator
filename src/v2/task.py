class Task:
    FAILED = "Failed"
    COMPLETED = "Completed"

    def __init__(self, task_id: int = None, num_stages: int = 2):
        self.id = task_id
        self.stage_id = None
        self.in_pipeline = True
        self.tries = 0
        self.outcomes = [None for _ in range(num_stages)]

    def set_outcome(self, stage_id, state):
        self.outcomes[stage_id] = state
        self.stage_id = stage_id

    def get_outcome(self, stage_id):
        return self.outcomes[stage_id]
    
    def set_out_pipeline(self):
        self.in_pipeline = False

    def fully_complete(self) -> bool:
        for outcome in self.outcomes:
            if outcome != Task.COMPLETED:
                return False
        return True

    def __repr__(self):
        return f"<Task #{id(self)} {str(self.outcomes)}>"
