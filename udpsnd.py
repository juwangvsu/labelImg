import socket
import sys
sockaddr_local=("",14551)
HOST, PORT = "localhost", 14551
data = ''.join(sys.argv[1:])
#data='quit'
#data = "/media/student/code1/darknet/tagreal/images/frame0811.jpg"

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.bind(sockaddr_local)
# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
sock.sendto(data, (HOST, PORT))
#received = sock.recv(1024)

print "Sent:     {}".format(data)
#print "Received: {}".format(received)

