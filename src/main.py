from v2.pipeline import Pipeline
from v2.stage import Stage
from v2.simulation import Simulation

if __name__ == "__main__":
    pipeline = Pipeline([
        Stage(num_workers=1, speed_distribution=lambda: 2, precision_distribution=lambda: 0.5),
        Stage(num_workers=1, speed_distribution=lambda: 2, precision_distribution=lambda: 0.5),
    ])

    pipeline.add_tasks(10)

    simulation = Simulation(pipeline)
    simulation.run(50)
