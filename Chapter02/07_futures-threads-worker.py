# program desc
#   - worker using future
#   - performance is almost same to thread worker <- cuz it's using threadpool executor
#   - but its simpler than manual thread model
#   - and u can get faster result w/ only changing to processpoll executor
#     - in next example code
# purpose
#   - future way allows us to use 'functional' way
#     - compute()'s logic is now stateless
#       - dosen't access results []
from concurrent import futures
import random


def compute():
    return sum(
        [random.randint(1, 100) for i in range(1000000)])


with futures.ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(compute) for _ in range(8)]

results = [f.result() for f in futures]

print("Results: %s" % results)
