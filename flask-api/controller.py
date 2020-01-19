from testrepository import Repository

repo = Repository()


class Controller:
    def userRegistered(self, id):
        return repo.userRegistered(id)

    def getBalance(self, id):
        if self.userRegistered(id):
            return repo.getBalance(id)
        else:
            return None

    def changeBalance(self, id, amount):
        if not self.userRegistered(id):
            if amount < 0: return False
            
            repo.registerUser(id)
            repo.changeBalance(id, amount)
            return True
        else:
            currentBalance = repo.getBalance(id)
            if currentBalance + amount >= 0:
                repo.changeBalance(id, amount)
                return True
            else:
                return False


        repo.changeBalance(id, amount)
