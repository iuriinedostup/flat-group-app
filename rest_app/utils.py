from functools import wraps

from flask import request
from flask_restful import abort


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            resource = args[0]
            api_token = resource.config['API_TOKEN']
            token = request.headers.environ['HTTP_AUTHORIZATION']

            if token == 'Basic {}'.format(api_token):
                return func(*args, **kwargs)

        except KeyError:
            pass

        abort(401, message="API Token is required")

    return wrapper
