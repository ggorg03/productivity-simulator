import pandas as pd

from .task import Task


class TasksRecorder():
    __sample = 0
    __step = 0

    __record = pd.DataFrame.from_dict({ 
                                'sample_id': [],
                                'step': [],
                                'task_id': [],
                                'task_stage_id': [],
                                'task_status': [],
                                'task_tries': []
                            })
    
    def __init__(self) -> None:
        pass
    
    def set_context(self, current_sample: int, current_step: int):
        TasksRecorder.__sample = current_sample
        TasksRecorder.__step = current_step
    
    def get_record() -> pd.DataFrame:
        return TasksRecorder.record
    
    def record(self, task: Task) -> None:
        new_row = TasksRecorder.__task_to_new_record(task)
        TasksRecorder.__add_to_record(new_row)
    
    def record_all(self, tasks: list[Task]) -> None:
        for task in tasks:
            if(task.in_pipeline):
                self.record(task)
    
    def save_record(self, path: str, name: str) -> None:
        file_name = f'{name}.csv'
        TasksRecorder.__record.to_csv(f'{path}/{file_name}')
        TasksRecorder.__reset_state()
    
    @staticmethod
    def __add_to_record(new_row: pd.DataFrame) -> None:
        TasksRecorder.__record = pd.concat([TasksRecorder.__record, new_row], ignore_index=True)
    
    @staticmethod
    def __task_to_new_record(task: Task) -> pd.DataFrame:
        return  pd.DataFrame.from_dict({
            'sample_id': [TasksRecorder.__sample],
            'step': [TasksRecorder.__step],
            'task_id': [task.id],
            'task_stage_id': [task.stage_id],
            'task_status': [1 if task.fully_complete() else 0],
            'task_tries': [task.tries]
        })
    
    @staticmethod
    def __reset_state():
        TasksRecorder.__sample = 0
        TasksRecorder.__step = 0

        TasksRecorder.__record = pd.DataFrame.from_dict({ 
                                        'sample_id': [],
                                        'step': [],
                                        'task_id': [],
                                        'task_stage_id': [],
                                        'task_status': [],
                                        'task_tries': []
                                    })