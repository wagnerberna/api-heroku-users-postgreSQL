import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
POSTGRESQL_LOCALHOST = os.getenv('POSTGRESQL_LOCALHOST')
POSTGRESQL_HEROKU = os.getenv('POSTGRESQL_HEROKU')


# POSTGRESQL_LOCALHOST = "postgresql://postgres:123@localhost:5432/wb_db"
# POSTGRESQL_HEROKU = "postgres://ndxyrolnkefpxf:cc9f341cfcf4f8b076ee282ecb88872fe9578fa8c53ed495ff15ea6663178a8d@ec2-52-45-83-163.compute-1.amazonaws.com:5432/dbvld7vgp4pomg"
# DATABASE_URL = os.environ['DATABASE_URL']


class Postgresql:
    def postgresql_connect(self):
        try:
            connection = psycopg2.connect(POSTGRESQL_HEROKU, sslmode='require')
            # connection = psycopg2.connect(POSTGRESQL_HEROKU)

            return connection

        except:
            print('ERROR - Cannot connect to db')

    # add /update / delete
    def execute_modify(self, sql_query, data):
        connection = self.postgresql_connect()
        cursor = connection.cursor()
        cursor.execute(sql_query, data)
        connection.commit()
        count = cursor.rowcount
        # print(count)
        cursor.close()
        connection.close()
        return count

    # get_by_field
    # fetchone retorna uma tupla
    def fetch_one(self, sql_query, field):
        connection = self.postgresql_connect()
        cursor = connection.cursor()
        cursor.execute(sql_query, field)
        result = cursor.fetchone()
        print(result)
        cursor.close()
        connection.close()
        return result

    # get_all
    # fetchall retorna uma lista com tuplas, cada tupla contendo 1 linha da tabela
    def fetch_all(self, sql_query):
        connection = self.postgresql_connect()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        print("---db:::", result)
        # for row in result:
        #     print(row)
        cursor.close()
        connection.close()
        return result

    def execute_sql_many(self, sql, data):
        pass
