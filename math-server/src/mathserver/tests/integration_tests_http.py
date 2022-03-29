import requests
import os

HOST = os.getenv('HTTP_HOST', default='localhost')
PORT = os.getenv('HTTP_PORT', default='9000')


def test_calculate():
    """
    Testing the '/calculate' endpoint
    """
    # Valid operation
    response = requests.post(f'http://{HOST}:{PORT}/calculate', data={'string': 'add 1 2'})
    assert response.status_code == 200
    assert response.text == '3.0'

    # Valid operation
    response = requests.post(f'http://{HOST}:{PORT}/calculate', data={'string': 'SUB -10 -20'})
    assert response.status_code == 200
    assert response.text == '10.0'

    requests.post(f'http://{HOST}:{PORT}/calculate', data={'string': 'pow 9 2'})
    requests.post(f'http://{HOST}:{PORT}/calculate', data={'string': 'POW 100 0'})

    # Wrong operator
    response = requests.post(f'http://{HOST}:{PORT}/calculate', data={'string': 'abc 1 2'})
    assert response.status_code == 200
    assert response.text == ''

    # Incorrect operation
    response = requests.post(f'http://{HOST}:{PORT}/calculate', data={'string': 'MUL 2 dfg'})
    assert response.status_code == 200
    assert response.text == ''

    # Zero division
    response = requests.post(f'http://{HOST}:{PORT}/calculate', data={'string': 'TRUEDIV 1 0'})
    assert response.status_code == 200
    assert response.text == ''


def test_all_operations():
    """
    Testing the '/all_operations' endpoint
    """
    # Get request with json as a response
    response = requests.get(f'http://{HOST}:{PORT}/all_operations')
    assert response.headers.get('content-type') == 'application/json'
    assert response.json() == ['Operator.ADD, number1 = 1.0, number2 = 2.0, result = 3.0',
                               'Operator.SUB, number1 = -10.0, number2 = -20.0, result = 10.0',
                               'Operator.POW, number1 = 9.0, number2 = 2.0, result = 81.0',
                               'Operator.POW, number1 = 100.0, number2 = 0.0, result = 1.0']

    # Request with limit
    response = requests.get(f'http://{HOST}:{PORT}/all_operations', params={'limit': 2})
    assert response.json() == ['Operator.ADD, number1 = 1.0, number2 = 2.0, result = 3.0',
                               'Operator.SUB, number1 = -10.0, number2 = -20.0, result = 10.0']

    # Request with offset
    response = requests.get(f'http://{HOST}:{PORT}/all_operations', params={'offset': 1})
    assert response.json() == ['Operator.SUB, number1 = -10.0, number2 = -20.0, result = 10.0',
                               'Operator.POW, number1 = 9.0, number2 = 2.0, result = 81.0',
                               'Operator.POW, number1 = 100.0, number2 = 0.0, result = 1.0']

    # Request with limit and offset
    response = requests.get(f'http://{HOST}:{PORT}/all_operations', params={'limit': 2, 'offset': 1})
    assert response.json() == ['Operator.SUB, number1 = -10.0, number2 = -20.0, result = 10.0',
                               'Operator.POW, number1 = 9.0, number2 = 2.0, result = 81.0']


def test_all_operations_concrete():
    """
    Testing the '/all_operations/<operation>' endpoint
    """
    # All 'add' operations
    response = requests.get(f'http://{HOST}:{PORT}/all_operations/add')
    assert response.json() == ['Operator.ADD, number1 = 1.0, number2 = 2.0, result = 3.0']

    # All 'pow' operations
    response = requests.get(f'http://{HOST}:{PORT}/all_operations/pow')
    assert response.json() == ['Operator.POW, number1 = 9.0, number2 = 2.0, result = 81.0',
                               'Operator.POW, number1 = 100.0, number2 = 0.0, result = 1.0']

    # Invalid operator
    response = requests.get(f'http://{HOST}:{PORT}/all_operations/qwerty')
    assert response.text == 'Invalid operation!'

    # All 'truediv' operations (we have none of them)
    response = requests.get(f'http://{HOST}:{PORT}/all_operations/truediv')
    assert response.json() == []

    # Request with limit
    response = requests.get(f'http://{HOST}:{PORT}/all_operations/pow', params={'limit': 1})
    assert response.json() == ['Operator.POW, number1 = 9.0, number2 = 2.0, result = 81.0']

    # Request with offset
    response = requests.get(f'http://{HOST}:{PORT}/all_operations/pow', params={'offset': 1})
    assert response.json() == ['Operator.POW, number1 = 100.0, number2 = 0.0, result = 1.0']

    # Request with limit and offset
    response = requests.get(f'http://{HOST}:{PORT}/all_operations/pow', params={'limit': 2, 'offset': 0})
    assert response.json() == ['Operator.POW, number1 = 9.0, number2 = 2.0, result = 81.0',
                               'Operator.POW, number1 = 100.0, number2 = 0.0, result = 1.0']


def test_allowed_operations():
    """
    Testing the '/allowed_operations' endpoint
    """
    response = requests.get(f'http://{HOST}:{PORT}/allowed_operations')
    # Received some json with allowed operations
    assert response.headers.get('content-type') == 'application/json'
