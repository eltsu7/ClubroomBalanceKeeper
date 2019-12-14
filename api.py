from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from repository import Repository

parser = reqparse.RequestParser()
parser.add_argument("amount", type=int, help="Amount must be an integer!")
parser.add_argument("amount", required=True, help="Amount can't be empty!")

app = Flask(__name__)
api = Api(app)

repo = Repository()

class Balance(Resource):
    def get(self, id):
        balance = repo.getBalance(id)

        if balance == None:
            return "User not found", 404
        else:
            return  balance, 200
            


class AddBalance(Resource):
    def put(self, id):
        args = parser.parse_args()
        amount = args["amount"]

        # TODO better return value than bool
        success = repo.changeBalance(id, amount)

        if success: return "Balance changed", 200
        else: return "Balance could not be changed", 400


api.add_resource(Balance, "/balance/<string:id>")
api.add_resource(AddBalance, "/addbalance/<string:id>")

if __name__ == "__main__":
    app.run(debug=True)
