from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from controller import Controller

parser = reqparse.RequestParser()

app = Flask(__name__)
api = Api(app)

controller = Controller()

class User(Resource):
    def isTrusted(self, key):

        if key != "":
            with open('trusted_hosts') as f:
                trusted_keys = f.readlines()
                trusted_keys = [x.strip() for x in trusted_keys]
    
                return key in trusted_keys

        return False

    def get(self):

        user = request.args.get('user')
        api_key = request.args.get('api_key')

        print(user, api_key)

        if self.isTrusted(api_key):

            balance = controller.getBalance(str(user))    

            if balance == None:
                return "User not found", 404
            else:
                return  balance, 200
            


class Transaction(Resource):
    def put(self, id):
        args = parser.parse_args()
        amount = args["amount"]

        # TODO better return value than bool
        success = controller.changeBalance(str(id), int(amount))

        if success: return "Balance changed", 200
        else: return "Balance could not be changed", 400


api.add_resource(User, "/user")
api.add_resource(Transaction, "/transaction")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
