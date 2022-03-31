# HTTP-server
### Default port: 9000
## Endpoints:
* ### GET '/allowed_operations'
Response: json - all allowed operations with description

Example:
```json
{
    "add": "Same as a + b.",
    "copysign": "Return a float with the magnitude (absolute value) of x but the sign of y.\n\nOn platforms that support signed zeros, copysign(1.0, -0.0)\nreturns -1.0.\n",
    "floordiv": "Same as a // b.",
    "hypot": "hypot(*coordinates) -> value\n\nMultidimensional Euclidean distance from the origin to a point.\n\nRoughly equivalent to:\n    sqrt(sum(x**2 for x in coordinates))\n\nFor a two dimensional point (x, y), gives the hypotenuse\nusing the Pythagorean theorem:  sqrt(x*x + y*y).\n\nFor example, the hypotenuse of a 3/4/5 right triangle is:\n\n    >>> hypot(3.0, 4.0)\n    5.0\n",
    "log": "log(x, [base=math.e])\nReturn the logarithm of x to the given base.\n\nIf the base not specified, returns the natural logarithm (base e) of x.",
    "mod": "Same as a % b.",
    "mul": "Same as a * b.",
    "pow": "Same as a ** b.",
    "sub": "Same as a - b.",
    "truediv": "Same as a / b."
}
```


* ### POST '/calculate'
Parameter: 'string' (form data),

should be in format:

    {operator} {number1} {number2}

Response:
1. Float number if input data is correct
2. Empty string if input data is invalid

Examples:
1. string: 'add 100.3 321.7' -> response: '422.0'
2. string: 'MUL 123 0.01' -> response: '1.23'
3. string: 'POW aaa bbb' -> response: ''
4. string: 'TRUEDIV 999 0' -> response: ''

* ### GET '/all_operations'
Response: json - all handled operations

Parameters (url parameters, optional):
* 'limit'
* 'offset'

Examples:

Request: http://localhost:9000/all_operations

Response:
```json
[
    "Operator.FLOORDIV, number1 = 401.0, number2 = 100.0, result = 4.0",
    "Operator.POW, number1 = 99.0, number2 = 3.0, result = 970299.0",
    "Operator.ADD, number1 = 100.3, number2 = 321.7, result = 422.0",
    "Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23",
    "Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23",
    "Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23"
]
```
Request: http://localhost:9000/all_operations?limit=3

Response:
```json
[
    "Operator.FLOORDIV, number1 = 401.0, number2 = 100.0, result = 4.0",
    "Operator.POW, number1 = 99.0, number2 = 3.0, result = 970299.0",
    "Operator.ADD, number1 = 100.3, number2 = 321.7, result = 422.0"
]
```
Request: http://localhost:9000/all_operations?offset=2

Response:
```json
[
    "Operator.ADD, number1 = 100.3, number2 = 321.7, result = 422.0",
    "Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23",
    "Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23",
    "Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23"
]
```
Request: http://localhost:9000/all_operations?limit=2&offset=1

Response:
```json
[
    "Operator.POW, number1 = 99.0, number2 = 3.0, result = 970299.0",
    "Operator.ADD, number1 = 100.3, number2 = 321.7, result = 422.0"
]
```
* ### GET '/all_operations/&lt;operation>'

Response: json - all handled **concrete** operations

Parameters:
* 'operation' (path variable)
* 'limit' (url parameter)
* 'offset' (url parameter)

Examples:

Request: http://localhost:9000/all_operations/add

Response:
```json
[
    "Operator.ADD, number1 = 100.3, number2 = 321.7, result = 422.0"
]
```
Request: http://localhost:9000/all_operations/log

Response:
```json
[]
```
Request: http://localhost:9000/all_operations/mul?limit=2

Response:
```json
[
    "Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23",
    "Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23"
]
```
Request: http://localhost:9000/all_operations/mul?offset=2

Response:
```json
[
    "Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23"
]
```
Request: http://localhost:9000/all_operations/mul?limit=0&offset=3

Response:
```json
[]
```
# Socket-server
### Default port: 8000
## Usage:

* ### 'allowed_operations'
Response: list of allowed operations

Example:

    'copysign, floordiv, log, hypot, truediv, sub, pow, mod, mul, add'

* ### Calculation

Send a string in format:

    {operator} {number1} {number2}

Response:
1. Float number if input data is correct
2. Empty string is input data is invalid

Examples:
1. 'truediv 33 11' -> response: '3.0'
2. 'LOG 1024 2' -> response: '10.0'
3. 'hypot qwe 321' -> response: ''
4. '' -> response: ''

* ### 'all_operations'
* ### 'all_operations -limit {limit}'
* ### 'all_operations -offset {offset}'
* ### 'all_operations -limit {limit} -offset {offset}'

Response: list os all handled operations

Examples:

String: 'all_operations'

Response:

    'Operator.FLOORDIV, number1 = 401.0, number2 = 100.0, result = 4.0, 
    Operator.POW, number1 = 99.0, number2 = 3.0, result = 970299.0, 
    Operator.ADD, number1 = 100.3, number2 = 321.7, result = 422.0, 
    Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23, 
    Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23, 
    Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23'

String: 'all_operations -limit 3'

Response:

    'Operator.FLOORDIV, number1 = 401.0, number2 = 100.0, result = 4.0, 
    Operator.POW, number1 = 99.0, number2 = 3.0, result = 970299.0, 
    Operator.ADD, number1 = 100.3, number2 = 321.7, result = 422.0'

String: 'all_operations -offset 2'

Response:

    'Operator.ADD, number1 = 100.3, number2 = 321.7, result = 422.0, 
    Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23, 
    Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23, 
    Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23'

String: 'all_operations -limit 1 -offset 1'

Response:

    'Operator.POW, number1 = 99.0, number2 = 3.0, result = 970299.0'

* ### 'all_operations {operation}'
* ### 'all_operations {operation} -limit {limit}'
* ### 'all_operations {operation} -offset {offset}'
* ### 'all_operations {operation} -limit {limit} -offset {offset}'

Response: list os all **concrete** handled operations

Examples:

String: 'all_operations floordiv'

Response:

    'Operator.FLOORDIV, number1 = 401.0, number2 = 100.0, result = 4.0'

String: 'all_operations mul -limit 2'

Response:

    'Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23, 
    Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23'

String: 'all_operations mul -offset 2'

Response:

    'Operator.MUL, number1 = 123.0, number2 = 0.01, result = 1.23'

String: 'all_operations mul -limit 0 -offset 2'

Response:

    ''