from v2.pipeline import Pipeline
from v2.stage import Stage
from v2.simulation import Simulation

import pandas as pd

if __name__ == "__main__":
    dataset = {
        "total_tasks": [],
        "completed_tasks": []
    }

    task_count = 10000
    total_steps = 1000

    for _ in range(0, 100):
        pipeline = Pipeline([
            Stage(num_workers=5, speed_distribution=lambda: 1, precision_distribution=lambda: 0.9),
            Stage(num_workers=5, speed_distribution=lambda: 1, precision_distribution=lambda: 0.9),
            Stage(num_workers=5, speed_distribution=lambda: 1, precision_distribution=lambda: 0.9),
            Stage(num_workers=5, speed_distribution=lambda: 1, precision_distribution=lambda: 0.9)
        ], task_count)

        simulation = Simulation(pipeline)
        completed_count = simulation.run(total_steps)

        dataset["total_tasks"].append(task_count)
        dataset["completed_tasks"].append(completed_count)

    dataset = pd.DataFrame.from_dict(dataset)

    dataset.to_csv('results.csv')