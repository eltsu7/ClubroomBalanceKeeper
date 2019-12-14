class Repository:

    def __init__(self):
        self.balances = {
            "123": 300,
            "moi": 200
        }

    def userRegistered(self, id):
        return str(id) in self.balances


    def getBalance(self, id):
        if self.userRegistered(id):
            return self.balances[str(id)]


    def changeBalance(self, id, amount):
        amount = int(amount)

        # existing user
        if self.userRegistered(id):
            # not enough balance
            if amount + self.balances[id] < 0:
                return False
            else:
                self.balances[id] += amount
                return True

        # new user
        else:
            if amount > 0:
                self.balances[id] = amount
                return True