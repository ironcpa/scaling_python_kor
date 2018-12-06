# program desc
#   - using 'rq' queue for distributed worker
#   - but this just enqueue to queue and nothing happened.
# how to run
#   - run this script
#   - run 'rq worker' in other terminal
#   - u can see the enqueued values in worker's terminal
import time

from rq import Queue
from redis import Redis

q = Queue(connection=Redis())

job = q.enqueue(sum, [42, 43])
while job.result is None:
    time.sleep(1)
    print('wait until job done')

print(job.result)
