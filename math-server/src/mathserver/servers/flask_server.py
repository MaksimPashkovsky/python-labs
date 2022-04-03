import os
from flask import Flask, request, jsonify
from ..models import Note
from ..calc import do_calculation
from ..operators import ALLOWED_OPERATIONS, Operator
from ..db_setup import session
import multiprocessing

app = Flask(__name__)


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.form["string"]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=do_calculation, args=(data, q))
    p.start()
    p.join()
    # en, num1, num2, result = do_calculation(data)
    en, num1, num2, result = q.get()
    if isinstance(result, float) or isinstance(result, int):
        try:
            note = Note(en, num1, num2, result)
            session.add(note)
            session.commit()
        except Exception:
            return ''
    return str(result)


@app.route('/all_operations', defaults={'operation': None}, methods=['GET'])
@app.route('/all_operations/<operation>', methods=['GET'])
def all_operations(operation):
    limit = request.args.get('limit', None)
    offset = request.args.get('offset', None)

    if operation is None:
        query = session.query(Note) \
            .limit(limit) \
            .offset(offset)
        return jsonify(list(map(str, query)))

    operation = operation.upper()
    if operation in Operator.__members__:
        query = session.query(Note) \
            .filter(Note.operator == Operator[operation]) \
            .limit(limit) \
            .offset(offset)
        return jsonify(list(map(str, query)))
    else:
        return 'Invalid operation!'


@app.route('/allowed_operations', methods=['GET'])
def allowed_operations():
    return jsonify({op.__name__: op.__doc__ for op in ALLOWED_OPERATIONS})


if __name__ == '__main__':
    app.run(host=os.getenv('HTTP_HOST', default='0.0.0.0'),
            port=os.getenv('HTTP_PORT', default=9000), debug=True)
