# program desc
#   - blocking socket simulation w/ http delay feature
#     - send http request to an web server and get response after 5 sec
#     - show print delayed about 5 sec
import socket

s = socket.create_connection(("httpbin.org", 80))
s.send(b"GET /delay/5 HTTP/1.1\r\nHost: httpbin.org\r\n\r\n")
buf = s.recv(1024)
print(buf)
