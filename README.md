# productivity-simulator

Simulates agents working in a task pipeline.

Each task must pass through every stage of the pipeline.
After an agent works on a task, the stage worked on can be set as completed or failed.
The task then moves to the next stage of the pipeline, where an agent from that stage receives the task.
If the agent detects an error in the task, they send the task back to be fixed.

Each agent has two attributes affecting how they process tasks: speed and precision.
Speed affects the number of tasks worked per simulation step.
Precision affects the chance of failing or completing a task.

An agent's speed and precision might improve as the simulation progresses.
The improved attribute is determined by the agent's focus:
speed agents improve their speed, precision agents improve their precision.