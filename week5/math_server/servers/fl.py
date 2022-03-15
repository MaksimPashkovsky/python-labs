from flask import Flask, request
from ..calc import do_calculation

app = Flask(__name__)


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.form["string"]
    result = do_calculation(data)
    return result
