from flask import Flask
from flask_restful import Resource, Api, abort
from flask import request

from src.models import RandomForestModel

app = Flask(__name__)
api = Api(app)


class Predictor(Resource):
    def __init__(self):
        self.model = RandomForestModel()
        self.model.load('models/random_forest.model')

    def post(self):
        json = request.get_json()
        try:
            x0 = json['data']['x0']
            x1 = json['data']['x1']
            x2 = json['data']['x2']
            x3 = json['data']['x3']
        except (TypeError, ValueError):
            return abort(400, description='Invalid arguments')

        return {'class': self.model.predict([[x0, x1, x2, x3]])[0]}


api.add_resource(Predictor, '/ask')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
