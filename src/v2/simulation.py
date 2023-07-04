from .task import Task
from .worker import Worker


def run():
    workers = [
        Worker(0),
        Worker(1)
    ]

    tasks = [
        Task(),
        Task()
    ]

    for task in tasks:
        for worker in workers:
            worker.work(task)

    print(tasks)
