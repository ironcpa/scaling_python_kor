# deamon의 의미
#   - deamon thread is background thread
#   - if parent thread ends, daemon killed before complete
#   - not exactly same w/ .join()
#     - you can check diff w/ sleep()

import threading
import time


def print_something(something):
    time.sleep(1)
    print(something)


t = threading.Thread(target=print_something, args=("hello",))
t.daemon = True
t.start()
print("thread started")
