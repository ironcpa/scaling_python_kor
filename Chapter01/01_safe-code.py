import threading

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# this code shows what the GIL means in python
# this code is threadsafe cuz of GIL
#   always print [2, 1]
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

x = []

def append_two(l):
    l.append(2)

threading.Thread(target=append_two, args=(x,)).start()

x.append(1)
print(x)
