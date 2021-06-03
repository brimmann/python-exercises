import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen(5)
while True:
	clt, adr = s.accept()
	print("connection to" + str(adr) + "established:")
	clt.send(b'Welcom to socket programming in python')
	#s.close()
	
