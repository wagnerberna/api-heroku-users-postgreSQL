import psycopg2

# POSTGRESQL_SERVER = "postgres://ndxyrolnkefpxf:cc9f341cfcf4f8b076ee282ecb88872fe9578fa8c53ed495ff15ea6663178a8d@ec2-52-45-83-163.compute-1.amazonaws.com:5432/dbvld7vgp4pomg"
POSTGRESQL_SERVER = "postgresql://postgres:123@localhost:5432/wb_db"
connection = psycopg2.connect(POSTGRESQL_SERVER)
# connection = psycopg2.connect(host="localhost", database="wb_db", user="postgres", password="123", port=5432)
# print(connection)

# passar script com dados
sql = """INSERT INTO db.user (name, email, login, password, activated) VALUES (%s,%s,%s,%s,%s)"""
data_to_insert = ("Cris", "cris@mail.com", "cris", "123", True)

cursor = connection.cursor()
cursor.execute(sql, data_to_insert)

# iserir dados direto
cursor.execute("INSERT INTO db.user VALUES (2 'wagner', 'w@mail.com', 'wag_teste', '123', True)")
connection.commit()
count = cursor.rowcount
print(count)
cursor.close()
connection.close()
