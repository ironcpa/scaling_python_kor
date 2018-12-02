# program desc
#   - show one way to use nonblocking socket properly
#   - in this case use select module
#     - check w/ ready_to_read flag
# side note
#   - select has it's own blocking time inside
#     - if you avoid this block, set 0 as last arg in select.select()
#       - but is's not recommandable to use 0 in real life
#       - just depend on select's default in real life
import select
import socket

s = socket.create_connection(("httpbin.org", 80))
s.setblocking(False)
s.send(b"GET /delay/1 HTTP/1.1\r\nHost: httpbin.org\r\n\r\n")
while True:
    print('.', end='')
    ready_to_read, ready_to_write, in_error = select.select(
        [s], [], [], 0)   # set 0 timeout to test no delay to check non-blocking
    if s in ready_to_read:
        buf = s.recv(1024)
        print(buf)
        break
'''
ready_to_read, ready_to_write, in_error = select.select(
    [s], [], [])
if s in ready_to_read:
    buf = s.recv(1024)
    print(buf)
    '''
