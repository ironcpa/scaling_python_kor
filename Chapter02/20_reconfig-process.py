# program desc
#   - process reconfigure feature of cotyledon
#     - it is possible to reconfigure worker count during runtime 
#   - in this example
#     - u can send signal to reconfigure
#       $ kill -HUP <pid>
#     - example run
#       $ ps ax | grep 20_reconfig
#       27384 pts/21   Sl+    0:00 20_reconfig-process.py: master process [20_reconfig-process.py]
#       27386 pts/21   Sl+    0:00 20_reconfig-process.py: master process [20_reconfig-process.py]
#       27392 pts/21   Sl+    0:00 20_reconfig-process.py: ProducerService worker(0)
#       27397 pts/21   Sl+    0:00 20_reconfig-process.py: printer worker(0)
#       27402 pts/21   Sl+    0:00 20_reconfig-process.py: printer worker(1)
#       $ kill -HUP 27384
#       $ ps ax | grep 20_reconfig
#       27384 pts/21   Sl+    0:00 20_reconfig-process.py: master process [20_reconfig-process.py]
#       27386 pts/21   Sl+    0:00 20_reconfig-process.py: master process [20_reconfig-process.py]
#       27548 pts/21   Sl+    0:00 20_reconfig-process.py: printer worker(0)
#       27553 pts/21   Sl+    0:00 20_reconfig-process.py: ProducerService worker(0)
#       27558 pts/21   Sl+    0:00 20_reconfig-process.py: printer worker(1)
#       27563 pts/21   Sl+    0:00 20_reconfig-process.py: printer worker(2)
#       27568 pts/21   Sl+    0:00 20_reconfig-process.py: printer worker(3)
#       27573 pts/21   Sl+    0:00 20_reconfig-process.py: printer worker(4)
import multiprocessing
import time

import cotyledon


class Manager(cotyledon.ServiceManager):
    def __init__(self):
        super(Manager, self).__init__()
        queue = multiprocessing.Manager().Queue()
        self.add(ProducerService, args=(queue,))
        self.printer = self.add(PrinterService, args=(queue,), workers=2)
        self.register_hooks(on_reload=self.reload)

    def reload(self):
        print("Reloading")
        self.reconfigure(self.printer, 5)


class ProducerService(cotyledon.Service):
    def __init__(self, worker_id, queue):
        super(ProducerService, self).__init__(worker_id)
        self.queue = queue

    def run(self):
        i = 0
        while True:
            self.queue.put(i)
            i += 1
            time.sleep(1)


class PrinterService(cotyledon.Service):
    name = "printer"

    def __init__(self, worker_id, queue):
        super(PrinterService, self).__init__(worker_id)
        self.queue = queue

    def run(self):
        while True:
            job = self.queue.get(block=True)
            print("I am Worker: %d PID: %d and I print %s"
                % (self.worker_id, self.pid, job))


Manager().run()
