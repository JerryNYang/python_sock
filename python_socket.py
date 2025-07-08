import socket


# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to a specific address and port
server_address = ('localhost', 1234)
server_socket.bind(server_address)


# Listen for incoming connections
server_socket.listen(5)


while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()


    # Receive and send data
    data = client_socket.recv(1024)
    client_socket.send(b"Received: " + data)


    # Close the client socket
    client_socket.close()




#SOCKETS - Sockets can be used to connect two nodes together.  
#import socket

#HOST = '127.0.0.1'
#PORT = 7777

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock stream is a port
#s.connect((HOST,PORT))


#nc -nvlp 7777
