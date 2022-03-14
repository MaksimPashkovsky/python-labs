"""
Математический socket-сервер
"""

import socketserver
import os
from dotenv import load_dotenv
from ..calc import do_calculation


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        self.data = self.request.recv(1024).strip()
        data = self.data.decode('utf-8')
        print(f"Received: {data}")
        result = do_calculation(data)
        self.request.sendall(str(result).encode('utf-8'))


if __name__ == '__main__':
    load_dotenv()
    HOST, PORT = os.getenv('SOCKET').split(':')
    with socketserver.TCPServer((HOST, int(PORT)), MyTCPHandler) as server:
        print(f"Server {server.server_address} listening...")
        server.serve_forever()
