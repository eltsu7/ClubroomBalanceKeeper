from os import environ
import psycopg2


class Repository:

    def open_connection(self):
        db_name = environ["PSQL_DB"]
        db_user = environ["PSQL_USER"]
        db_pass = ""
        db_host = environ["PSQL_HOST"]
        db_port = environ["PSQL_PORT"]

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
        conn = self.open_connection()
        if not conn:
            return None

        cursor = conn.cursor()

        sql =   "SELECT 1 " \
                "FROM user " \
                "WHERE user_id = {};"

        cursor.execute(sql.format(id))

        registered = cursor.fetchone() is not None

        conn.close()

        return registered


    def registerUser(self, id):
        self.balances[id] = 0

    def getBalance(self, id):
        return self.balances[str(id)]

    def changeBalance(self, id, amount):
        self.balances[id] += amount
