from database import get_db_connection as get_connection


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists employee (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            age INT,
            department VARCHAR(50),
            salary NUMERIC,
            is_manager BOOLEAN DEFAULT FALSE,
            managed_department VARCHAR(50)
        );
                """)
    conn.commit()
    cur.close()
    conn.close()
    print("Table created successfully.")
if __name__ == "__main__":
    create_table()
