from os import environ
import psycopg2


class Repository:

    def open_connection(self):
        db_name = environ["PSQL_DB"]
        db_user = environ["PSQL_USER"]
        db_pass = environ["PSQL_PASSWORD"]
        db_host = environ["PSQL_HOST"]
        db_port = environ["PSQL_PORT"]

        self.table_product = environ["PSQL_TABLE_PRODUCT"]
        self.table_user = environ["PSQL_TABLE_USER"]
        self.table_transaction = environ["PSQL_TABLE_TRANSACTION"]

        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_pass,
            host=db_host,
            port=db_port    
        )

        if conn.closed == 0:
            return conn
        else:
            return False


    def userRegistered(self, id):
        return str(id) in self.balances

    def registerUser(self, id):
        self.balances[id] = 0

    def getBalance(self, id):
        return self.balances[str(id)]

    def changeBalance(self, id, amount):
        self.balances[id] += amount
