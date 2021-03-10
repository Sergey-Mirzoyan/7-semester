#socket_echo_server.py
import socket
import sys


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to the port
server_address = ('localhost', 8001)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)


###
# Connect the socket to the port where the server is listening

###


# Listen for incoming connections


while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(64)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                #connection.sendall(data)
            else:
                print('no data from', client_address)
                break
    finally:
        
        
        # Clean up the connection
        #server_address2 = ('localhost', 9999)
        #print('connecting to {} port {}'.format(*server_address2))
        #cock.connect(server_address2)

        # Send data
        #message = b'SERVER 1 works hard'
        #print('sending {!r}'.format(message))
        #cock.sendall(message)

        # Look for the response
        #amount_received = 0
        #amount_expected = len(message)

        #while amount_received < amount_expected:
         #   data = cock.recv(16)
          #  amount_received += len(data)
           # print('received {!r}'.format(data))
        connection.close()
        
    
    
    try:

        # Send data
        server_address2 = ('localhost', 9999)
        print('connecting to {} port {}'.format(*server_address2))
        cock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cock.connect(server_address2)
        message = b'This is the message.  It will be repeated.'
        print('sending {!r}'.format(message))
        cock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = cock.recv(64)
            amount_received += len(data)
            print('received {!r}'.format(data))

    finally:
        print('closing socket')
        cock.close()