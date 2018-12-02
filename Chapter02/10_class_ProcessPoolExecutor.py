# program desc
#   - this code is just a clip of api codes
#     - not executable
#   - to show default worker count
class ProcessPoolExecutor(_base.Executor):
    def __init__(self, max_workers=None):
        # [...]
        if max_workers is None:
            self._max_workers = multiprocessing.cpu_count()
        else:
            self._max_workers = max_workers
