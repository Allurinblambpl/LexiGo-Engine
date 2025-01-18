import socket

class Network:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        self.client, self.address = self.socket.accept()

    def send_data(self, data):
        """Send data to the connected client."""
        self.client.sendall(data.encode('utf-8'))

    def receive_data(self):
        """Receive data from the connected client."""
        data = self.client.recv(1024)
        return data.decode('utf-8')

    def close(self):
        """Close the connection."""
        self.client.close()
        self.socket.close()
