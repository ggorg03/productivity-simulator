from .worker import Worker


def simulate_step(workers: list[Worker]):
    for worker in workers:
        worker.work()


def simulate(workers: list[Worker], steps: int):
    for step in range(0, steps):
        simulate_step(workers)


def generate_workers() -> list[Worker]:
    return [
        Worker(1, 0.5)
    ]


workers = generate_workers()
simulate(workers, 100)