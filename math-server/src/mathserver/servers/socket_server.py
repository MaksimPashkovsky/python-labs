import socketserver
import os
from ..operators import Operator, ALLOWED_OPERATIONS
from ..calc import do_calculation
from ..models import Note
from ..db_setup import session
import multiprocessing
import threading


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        self.data = self.request.recv(1024).strip()
        data = self.data.decode('utf-8')
        print(f"Received: {data}")

        tokens = data.split()

        if tokens[0] == 'allowed_operations':
            a = [n.__name__ for n in ALLOWED_OPERATIONS]
            self.request.sendall(', '.join(a).encode('utf-8'))
            return

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
            if len(tokens) != 1 and tokens[1].isalpha():
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

        q = multiprocessing.Queue()
        p = multiprocessing.Process(target=do_calculation, args=(data, q))
        p.start()
        p.join()
        en, num1, num2, result = q.get()
        if isinstance(result, float) or isinstance(result, int):
            note = Note(en, num1, num2, result)
            session.add(note)
            session.commit()
        self.request.sendall(str(result).encode('utf-8'))

    def finish(self) -> None:
        session.close()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == '__main__':
    HOST = os.getenv('SOCKET_HOST', '0.0.0.0')
    PORT = os.getenv('SOCKET_PORT', '8000')

    with ThreadedTCPServer((HOST, int(PORT)), MyTCPHandler) as server:
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        server_thread.join()
        server.shutdown()
