# program desc
#   - show basic usage of futurist package's periodic worker
#   - add 2 kind of workers
#     - 1: every_one : show elapsed time from started
#       - every 1 second
#     - 2: print worker stats
#       - every 4 second
import time

from futurist import periodics


@periodics.periodic(1)
def every_one(started_at):
    print("1: %s" % (time.time() - started_at))


w = periodics.PeriodicWorker([
    (every_one, (time.time(),), {}),
])


@periodics.periodic(4)
def print_stats():
    print("stats: %s" % list(w.iter_watchers()))


w.add(print_stats)
w.start()
