from .task import Task
from .worker import Worker


def run():
    workers = [
        Worker(0, 0.5),
        Worker(1, 0.5)
    ]

    tasks = [
        Task(),
        Task()
    ]

    for task in tasks:
        for worker in workers:
            worker.work(task)

    print(tasks)
