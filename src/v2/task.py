class Task:
    FAILED = "Failed"
    COMPLETED = "Completed"

    def __init__(self, num_stages: int = 2):
        self.state_by_stage = [None for _ in range(num_stages)]

    def set_outcome(self, stage_id, state):
        self.state_by_stage[stage_id] = state

    def get_outcome(self, stage_id):
        return self.state_by_stage[stage_id]

    def has_outcome(self, stage_id):
        return self.state_by_stage[stage_id] is not None

    def __repr__(self):
        return f"<Task #{id(self)} {str(self.state_by_stage)}>"
