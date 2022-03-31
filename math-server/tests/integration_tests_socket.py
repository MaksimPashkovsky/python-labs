import pytest
import os
import socket

HOST = os.getenv('SOCKET_HOST', default='localhost')
PORT = os.getenv('SOCKET_PORT', default='8000')


def send_to_socket(string: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, int(PORT)))
        s.sendall(string.encode('utf-8'))
        data = s.recv(1024)
        return data.decode('utf-8')


def test_calculation():
    """
    Testing the basic functional of socket server
    """

    # Correct data
    response = send_to_socket('add 1 2')
    assert response == '3.0'

    response = send_to_socket('MUL 12 0.5')
    assert response == '6.0'

    response = send_to_socket('MUL 15 3')
    assert response == '45.0'

    # Incorrect operation
    response = send_to_socket('aaa 15.2 3')
    assert response == ''

    # Incorrect data
    response = send_to_socket('MUL 15.2 3qwe')
    assert response == ''

    # Zero division
    response = send_to_socket('truediv 123 0')
    assert response == ''


def test_all_operations():
    # Getting all operations
    response = send_to_socket('all_operations')
    assert response == 'Operator.ADD, number1 = 1.0, number2 = 2.0, result = 3.0, ' \
                       'Operator.MUL, number1 = 12.0, number2 = 0.5, result = 6.0, ' \
                       'Operator.MUL, number1 = 15.0, number2 = 3.0, result = 45.0'

    # With limit
    response = send_to_socket('all_operations -limit 2')
    assert response == 'Operator.ADD, number1 = 1.0, number2 = 2.0, result = 3.0, ' \
                       'Operator.MUL, number1 = 12.0, number2 = 0.5, result = 6.0'

    # With offset
    response = send_to_socket('all_operations -offset 1')
    assert response == 'Operator.MUL, number1 = 12.0, number2 = 0.5, result = 6.0, ' \
                       'Operator.MUL, number1 = 15.0, number2 = 3.0, result = 45.0'

    # With limit and offset
    response = send_to_socket('all_operations -limit 1 -offset 1')
    assert response == 'Operator.MUL, number1 = 12.0, number2 = 0.5, result = 6.0'


def test_all_operations_concrete():
    # Getting all 'add' operations
    response = send_to_socket('all_operations add')
    assert response == 'Operator.ADD, number1 = 1.0, number2 = 2.0, result = 3.0'

    # Getting all 'mul' operations
    response = send_to_socket('all_operations mul')
    assert response == 'Operator.MUL, number1 = 12.0, number2 = 0.5, result = 6.0, ' \
                       'Operator.MUL, number1 = 15.0, number2 = 3.0, result = 45.0'

    # Getting all 'pow' operations (we have none of them)
    response = send_to_socket('all_operations pow')
    assert response == ''

    # With limit
    response = send_to_socket('all_operations mul -limit 1')
    assert response == 'Operator.MUL, number1 = 12.0, number2 = 0.5, result = 6.0'

    # With offset
    response = send_to_socket('all_operations mul -offset 1')
    assert response == 'Operator.MUL, number1 = 15.0, number2 = 3.0, result = 45.0'

    # With limit and offset
    response = send_to_socket('all_operations mul -limit 3 -offset 0')
    assert response == 'Operator.MUL, number1 = 12.0, number2 = 0.5, result = 6.0, ' \
                       'Operator.MUL, number1 = 15.0, number2 = 3.0, result = 45.0'
