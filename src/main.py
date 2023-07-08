from v2.pipeline import Pipeline
from v2.stage import Stage
from v2.simulation import Simulation
from v2.tasks_recorder import TasksRecorder

import pandas as pd
from tqdm import tqdm

if __name__ == "__main__":
    task_count = 100
    total_steps = 100
    
    groups = {
        'precision_group': {'speed': 3, 'precision': 0.85},
        'speed_group': {'speed': 6, 'precision': 0.7},
        'control_group': {'speed': 3, 'precision': 0.7}
    }

    for group, attributes in groups.items():
        tasks_recorder = TasksRecorder()
        
        for i in tqdm (range(0, 100), desc=f'{group}'):
            pipeline = Pipeline([
                Stage(num_workers=1,
                      speed_distribution=lambda: attributes['speed'],
                      precision_distribution=lambda: attributes['precision']
                ),Stage(num_workers=1,
                      speed_distribution=lambda: attributes['speed'],
                      precision_distribution=lambda: attributes['precision']
                ),Stage(num_workers=1,
                      speed_distribution=lambda: attributes['speed'],
                      precision_distribution=lambda: attributes['precision']
                )
            ], task_count)

            simulation = Simulation(id=i+1, pipeline=pipeline)
            simulation.run(total_steps)
        
        tasks_recorder.save_record('../samples', group)