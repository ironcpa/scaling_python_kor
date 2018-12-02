# program desc
#   - show simple usage of cotyledon service worker
#     - create 2 simple printer worker as service and run manager
# cotyledon service
#   - create master process
#   - create child worker processes
#   - below shell cmd show related process structures
#     $ ps ax | grep 18_cotyledon
#     25098 pts/21   Sl+    0:00 18_cotyledon.py: master process [18_cotyledon.py]
#     25101 pts/21   Sl+    0:00 18_cotyledon.py: printer worker(0)
#     25104 pts/21   Sl+    0:00 18_cotyledon.py: printer worker(1)
#   - cotyledon can resurrect crashed child processes
#   - communication btwn processes can be possible using queue -> in next example
import threading
import time

import cotyledon


class PrinterService(cotyledon.Service):
    name = "printer"

    def __init__(self, worker_id):
        super(PrinterService, self).__init__(worker_id)
        self._shutdown = threading.Event()

    def run(self):
        while not self._shutdown.is_set():
            print("Doing stuff")
            time.sleep(1)

    def terminate(self):
        self._shutdown.set()


# manager 생성
manager = cotyledon.ServiceManager()
# 2개의 PrinterService를 실행하기 위해 추가
manager.add(PrinterService, 2)
# manager에 추가된 작업을 모두 실행
manager.run()
