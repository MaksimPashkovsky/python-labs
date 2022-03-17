from flask import Flask, request, jsonify
from ..calc import do_calculation, ALLOWED_OPERATIONS

app = Flask(__name__)


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.form["string"]
    result = do_calculation(data)
    return result


@app.route('/operations', methods=['GET'])
def operations():
    return jsonify({op.__name__: op.__doc__ for op in ALLOWED_OPERATIONS})
