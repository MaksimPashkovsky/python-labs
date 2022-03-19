import socketserver
import os
from math_server.operators import Operator
from math_server.calc import do_calculation
from math_server.models import Note
from math_server.db_setup import init_db, session
init_db()


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        """
        Socket can receive strings:
        1) {operation} {number1} {number2}
        Sends the result of operation or '' in case of invalid input
        2) all_operations [operation] [-limit] [-offset]
        Sends the result of executed query
        """
        self.data = self.request.recv(1024).strip()
        data = self.data.decode('utf-8')
        print(f"Received: {data}")

        tokens = data.split()

        try:
            l_index = tokens.index('-limit')
            limit = tokens[l_index + 1]
        except (ValueError, IndexError):
            limit = None

        try:
            o_index = tokens.index('-offset')
            offset = tokens[o_index + 1]
        except (ValueError, IndexError):
            offset = None

        if tokens[0] == 'all_operations':
            if tokens[1].isalpha():
                operation = tokens[1].upper()
                if operation in Operator.__members__:
                    query = session.query(Note) \
                        .filter(Note.operator == Operator[operation]) \
                        .limit(limit) \
                        .offset(offset)
                    a = [str(n) for n in query]
                    self.request.sendall(', '.join(a).encode('utf-8'))
                    return
                else:
                    self.request.sendall('Invalid operation!'.encode('utf-8'))
                    return

            query = session.query(Note) \
                .limit(limit) \
                .offset(offset)
            a = [str(n) for n in query]
            self.request.sendall(', '.join(a).encode('utf-8'))
            return

        en, num1, num2, result = do_calculation(data)
        note = Note(en, num1, num2, result)
        session.add(note)
        session.commit()
        self.request.sendall(str(result).encode('utf-8'))


if __name__ == '__main__':
    HOST = os.getenv('SOCKET_HOST', 'localhost')
    PORT = os.getenv('SOCKET_PORT', '9090')

    with socketserver.TCPServer((HOST, int(PORT)), MyTCPHandler) as server:
        print(f"Server {server.server_address} listening...")
        server.serve_forever()
