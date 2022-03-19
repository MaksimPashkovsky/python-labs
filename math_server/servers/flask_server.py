from flask import Flask, request, jsonify
from ..models import Note
from ..calc import do_calculation
from ..operators import ALLOWED_OPERATIONS, Operator
from ..db_setup import init_db, session
init_db()

app = Flask(__name__)


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.form["string"]
    en, num1, num2, result = do_calculation(data)
    note = Note(en, num1, num2, result)
    session.add(note)
    session.commit()
    return str(result)


@app.route('/all_operations', defaults={'operation': None}, methods=['GET'])
@app.route('/all_operations/<operation>', methods=['GET'])
def all_operations(operation):

    limit = request.args.get('limit', None)
    offset = request.args.get('offset', None)

    if operation is None:
        query = session.query(Note)\
            .limit(limit)\
            .offset(offset)
        return jsonify(list(map(str, query)))

    operation = operation.upper()
    if operation in Operator.__members__:
        query = session.query(Note)\
            .filter(Note.operator == Operator[operation])\
            .limit(limit)\
            .offset(offset)
        return jsonify(list(map(str, query)))
    else:
        return 'Invalid operation!'


@app.route('/allowed_operations', methods=['GET'])
def allowed_operations():
    return jsonify({op.__name__: op.__doc__ for op in ALLOWED_OPERATIONS})
