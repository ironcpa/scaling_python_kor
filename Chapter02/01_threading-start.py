import threading
import time


def print_something(something):
    time.sleep(1)
    print(something)


t = threading.Thread(target=print_something, args=("hello",))
t.start()
print("thread started")
t.join()
