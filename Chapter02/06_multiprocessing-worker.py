# program desc
#   - process worker using pool
# purpose
#   - show pool's conveniance
#     - don't have to manually make collect machanism
#     - economical cuz internal process 'fork' call is reduced by using process pool
import multiprocessing
import random


def compute(n):
    return sum(
        [random.randint(1, 100) for i in range(1000000)])


# 8개의 워커를 시작한다.
pool = multiprocessing.Pool(processes=8)
print("Results: %s" % pool.map(compute, range(8)))
