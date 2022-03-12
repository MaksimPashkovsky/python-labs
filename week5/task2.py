"""
Математический socket-сервер
"""

import socketserver
import operator
import os
from dotenv import load_dotenv


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        self.data = self.request.recv(1024).strip()
        data = self.data.decode('utf-8')
        print(f"Received: {data}")
        try:
            operation, n1, n2 = data.split(' ')
            result = getattr(operator, operation)(float(n1), float(n2))
            print(f"Sending result: {result}")
            self.request.sendall(str(result).encode('utf-8'))
        except Exception:
            print('Incorrect input!')
            self.request.sendall(''.encode('utf-8'))


if __name__ == '__main__':
    load_dotenv('vars.env')
    HOST, PORT = os.getenv('SOCKET').split(':')
    with socketserver.TCPServer((HOST, int(PORT)), MyTCPHandler) as server:
        print(f"Server {server.server_address} listening...")
        server.serve_forever()
