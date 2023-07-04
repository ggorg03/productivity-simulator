class Task:
    FAILED = "Failed"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"

    def __init__(self):
        self.state_by_stage = dict()

    def set_stage_state(self, stage_id, state):
        self.state_by_stage[stage_id] = state

    def get_stage_state(self, stage_id):
        return self.state_by_stage[stage_id]

    def __repr__(self):
        return f"<Task #{id(self)} {str(self.state_by_stage)}>"