"""
Математический socket-сервер
"""

import socketserver
import os
from ..calc import do_calculation


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        self.data = self.request.recv(1024).strip()
        data = self.data.decode('utf-8')
        print(f"Received: {data}")
        result = do_calculation(data)
        self.request.sendall(str(result).encode('utf-8'))


if __name__ == '__main__':
    HOST = os.getenv('SOCKET_HOST', 'localhost')
    PORT = os.getenv('SOCKET_PORT', '9090')

    with socketserver.TCPServer((HOST, int(PORT)), MyTCPHandler) as server:
        print(f"Server {server.server_address} listening...")
        server.serve_forever()
