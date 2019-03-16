# -*- coding:utf-8 -*-
import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "test_db",
    user = "naoya",
    password="nashikui")

#conn.rollback()

cur = conn.cursor()

# try:
#     cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# except:
#     print("TABLE ALREADY EXISTS")

cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (200, "ghi_jkl"))

cur.execute("SELECT * FROM test;")
results = cur.fetchall()
print(results)

# auto commitではないので、明示的なcommitの実行が必要
conn.commit()
cur.close()
conn.close()
