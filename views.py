from flask import request, jsonify, Blueprint
from marshmallow import ValidationError


from utils import query_params


main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json
    try:
        cmd1 = data.get('cmd1')
        value1 = data.get('value1')
        cmd2 = data.get('cmd2')
        value2 = data.get('value2')

    except ValidationError as error:
        return jsonify(error.messages), 400

    result = None

    result = query_params(
        cmd1=cmd1,
        value1=value1,
        cmd2=cmd2,
        value2=value2,
        data=result,
        )
    return jsonify(result), 200



