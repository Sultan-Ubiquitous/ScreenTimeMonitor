import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

host = os.getenv("host")
dbname = os.getenv("dbname")
user = os.getenv("user")
password = os.getenv("password")
port = os.getenv("port")

# Schema:
# CREATE TABLE IF NOT EXISTS screen_time(
#     id SERIAL PRIMARY KEY,
#     app_name VARCHAR(255) NOT NULL,
#     duration INTEGER NOT NULL,
#     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP


def connect():
    conn = None
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
        return conn
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
        return None
        
        
def postAppData(app_name, duration):
    conn = connect()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()
        cur.execute("""
                    SELECT * FROM screen_time
                    WHERE app_name = %s AND DATE(timestamp) = CURRENT_DATE;
                    """, (app_name,))
        row = cur.fetchone()
        if row:
            cur.execute("""
                        UPDATE screen_time
                        SET duration = duration + %s
                        WHERE id = %s;
                        """, (duration, row[0]))
            
        else:
            cur.execute("""
                        INSERT INTO screen_time (app_name, duration)
                        VALUES(%s, %s) RETURNING id;
                        """, (app_name, duration))
    
        conn.commit()
        
        cur.close()
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            

if '__name__' == '__main__':
    postAppData("Google Chrome", 100)
    
