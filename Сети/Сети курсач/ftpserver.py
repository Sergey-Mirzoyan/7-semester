import socketserver
import socket

class Handler_TCPServer(socketserver.BaseRequestHandler):
    """
    The TCP Server class for demonstration.

    Note: We need to implement the Handle method to exchange data
    with TCP client.

    """

    def handle(self):
        # self.request - TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} sent:".format(self.client_address[0]))
        print(self.data)
        # just send back ACK for data arrival confirmation
        self.request.sendall("ACK from TCP Server".encode())

        
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    host_ip, server_port = "127.0.0.1", 9998
    data = " fine, thank you!\n"  
    # Init the TCP server object, bind it to the localhost on 9999 port
    tcp_server = socketserver.TCPServer((HOST, PORT), Handler_TCPServer)
    # Activate the TCP server.
    # To abort the TCP server, press Ctrl-C.
    
    
    
    

    try:
        #tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Establish connection to TCP server and exchange data
        tcp_client.connect((host_ip, server_port))
        tcp_client.sendall(data.encode())

        # Read data from the TCP server and close the connection
        received = tcp_client.recv(1024)
    finally:
        tcp_client.close()

    print ("Bytes Sent:     {}".format(data))
    print ("Bytes Received: {}".format(received.decode()))
    tcp_server.serve_forever()