import socket
import sys
import threading

HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket created")

try:
	s.bind((HOST, PORT))
except socket.error as msg:
	# print msg
	# print msg[0]
	# print msg[1]
	print ("Bind failed. Error Code : " + str(msg[0]) + " Message: " + msg[1])
	sys.exit()

print ("Socket bind complete")

s.listen(5)
print ("Socket now listening at %s:%s" %(HOST, PORT))

def handle_tcp(sock, addr):
	print("new connection from %s:%s" % addr)
	sock.send(b'Welcome!')

	while True:
		data = sock.recv(1024)
		if not data:
			break
		sock.send(b'Hello, %s!' % data)
	sock.close()


while True:
	print ("wait for connection...")
	sock, addr = s.accept()
	print (addr)
	t = threading.Thread(target=handle_tcp, args=(sock, addr))
	t.start()