import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE_LOCAL = os.getenv("DATABASE_LOCAL")
DATABASE_URL = os.getenv("DATABASE_URL")


class Postgresql:
    def postgresql_connect(self):
        try:
            connection = psycopg2.connect(DATABASE_URL, sslmode="require")
            return connection

        except:
            print("ERROR - Cannot connect to db")

    # add /update / delete
    def execute_modify(self, sql_query, data):
        connection = self.postgresql_connect()
        cursor = connection.cursor()
        cursor.execute(sql_query, data)
        connection.commit()
        count = cursor.rowcount
        cursor.close()
        connection.close()
        return count

    # get_by_field
    # fetchone return one tuple
    def fetch_one(self, sql_query, field):
        connection = self.postgresql_connect()
        cursor = connection.cursor()
        cursor.execute(sql_query, field)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result

    # get_all
    # fetchall return list for tuples, one line of table per tuple
    def fetch_all(self, sql_query):
        connection = self.postgresql_connect()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def execute_sql_many(self, sql, data):
        pass
