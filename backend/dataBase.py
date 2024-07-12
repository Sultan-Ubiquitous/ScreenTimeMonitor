import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

host = os.getenv("host")
dbname = os.getenv("dbname")
user = os.getenv("user")
password = os.getenv("password")
port = os.getenv("port")

conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
print("connection established!!")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS screen_time(
    id SERIAL PRIMARY KEY,
    app_name VARCHAR(255) NOT NULL,
    duration INTEGER NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
cur.close()
conn.close()
print("connection closed")