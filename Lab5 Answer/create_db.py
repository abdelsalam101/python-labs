import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

load_dotenv()

def create_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    conn.autocommit = True
    cur = conn.cursor()

    db_name = os.getenv("DB_NAME")
    cur.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier(db_name)
    ))

    print(f"Database '{db_name}' created successfully.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    create_database()
