class Task:
    FAILED = -1
    IN_PROGRESS = 0
    COMPLETED = 1

    def __init__(self):
        self.state_by_stage = dict()

    def set_stage_state(self, stage_id, state):
        self.state_by_stage[stage_id] = state

    def get_stage_state(self, stage_id):
        return self.state_by_stage[stage_id]
