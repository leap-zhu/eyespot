import json
import hashlib

from instafarm import app
from instafarm.models import model
from flask import Response, redirect, request, session

def json_response(obj, status=200):
    return Response(
        json.dumps(obj),
        status=status,
        mimetype='application/json')

def get_request(key, default_value=None):
    if key is None or key == '':
        return default_value
    value = request.values.get(key)
    if value is None and request.is_json:
        json_values = request.get_json()
        if json_values is not None and key in json_values:
            value = json_values[key]
    if value is None:
        value = default_value
    return value 

