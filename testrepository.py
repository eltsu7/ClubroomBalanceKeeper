class Repository:

    def __init__(self):
        self.balances = {
            "123": 300,
            "moi": 200
        }

    def userRegistered(self, id):
        return str(id) in self.balances

    def registerUser(self, id):
        self.balances[id] = 0

    def getBalance(self, id):
        return self.balances[str(id)]

    def changeBalance(self, id, amount):
        self.balances[id] += amount
