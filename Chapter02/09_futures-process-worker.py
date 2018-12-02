# program desc
#   - worker using future
#   - multiprocess performance by using processpool executor
#   - u can switch thread and process only by changing proper executors
#   - proper worker count == cpu core count
from concurrent import futures
import random


def compute():
    return sum(
        [random.randint(1, 100) for i in range(1000000)])


with futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(compute) for _ in range(20)]   # proper range is cpu core count

results = [f.result() for f in futures]

print("Results: %s" % results)
