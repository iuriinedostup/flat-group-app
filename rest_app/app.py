from flask import Flask
from flask_restful import Api

from rest_app.resources import HealthCheckResource
from rest_app.resources import FlatGroupResource
from rest_app.settings import conf

app = Flask(__name__)
api = Api(app)


api.add_resource(
    HealthCheckResource,
    '/status',
    resource_class_kwargs={
        'config': conf
    }
)

api.add_resource(
    FlatGroupResource,
    '/group',
    resource_class_kwargs={
        'config': conf
    }
)
