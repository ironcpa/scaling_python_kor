# program desc
#   - same to 03_multithreading-worker
#   - only diff is using process instead of thread
# purpose
#   - to check how faster process is than thread in python
import random
import multiprocessing


def compute(results):
    results.append(sum(
        [random.randint(1, 100) for i in range(1000000)]))


with multiprocessing.Manager() as manager:
    results = manager.list()
    workers = [multiprocessing.Process(target=compute, args=(results,))
            for x in range(8)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    print("Results: %s" % results)
