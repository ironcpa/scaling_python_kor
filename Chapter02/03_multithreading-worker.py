# program desc
#   - create 5 worker threads
#   - each worker sum lots of numbers
#   - and appends to results []
#     - worker thread directly access collector obj(results)
# purpose
#   - shows how to use workers
#   - and collect results from worker
# how to run w/ time profiling
#   $ /usr/bin/time -f "%Us user %Ss system %P cpu %e total" python 03_multithreading-worker.py
#   Results: [50476790, 50525415, 50485042, 50505938, 50518650, 50489051, 50522434, 50489569]
#   8.32s user 0.08s system 101% cpu 8.30 total
import random
import threading

results = []


def compute():
    results.append(sum(
        [random.randint(1, 100) for i in range(1000000)]))


workers = [threading.Thread(target=compute) for x in range(8)]
for worker in workers:
    worker.start()
for worker in workers:
    worker.join()
print("Results: %s" % results)
