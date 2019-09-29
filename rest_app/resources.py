import logging

from flask import make_response, jsonify, request
from flask_restful import Resource

from lib.grouper import FlatGroup
from lib.grouper import FlatGroupError

from rest_app.utils import auth_required

logger = logging.getLogger(__name__)


class BaseResource(Resource):

    def __init__(self, config):
        self.config = config


class HealthCheckResource(BaseResource):

    def get(self):
        return make_response(
            jsonify({'status': 'ok'}), 200)


class FlatGroupResource(BaseResource):

    @auth_required
    def post(self):
        keys = request.args.getlist('key', str)
        data = request.get_json()

        logger.info('grouping data by %s', keys)
        try:
            flat_group = FlatGroup(keys)
            data = flat_group.group(data)
        except FlatGroupError as e:
            return make_response(
                jsonify({'status': False, 'message': str(e)}),
                401
            )

        return make_response(jsonify(data), 200)
