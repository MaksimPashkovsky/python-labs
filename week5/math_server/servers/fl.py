from flask import Flask
from ..calc import do_calculation

app = Flask(__name__)


@app.route('/<data>')
def receive_string(data):
    result = do_calculation(data)
    return result
