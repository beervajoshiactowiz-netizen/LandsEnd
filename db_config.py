import mysql.connector

#sql connection
def make_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='actowiz',
        database='landsEnd_db'
    )
    return conn

#create tables
def create_table(table_name):
    q=f"""
        create table if not exists {table_name} (
        id  INT PRIMARY KEY AUTO_INCREMENT,
        prodUrl VARCHAR(500),
        product_name VARCHAR(100),
        brand VARCHAR(100),
        product_id  bigint,
        variants TEXT
        )
        """
    conn = make_connection()
    cursor = conn.cursor()
    cursor.execute(q)  #execute query
    conn.commit()
    conn.close()

#insert int otable by taking table name, and the data
def insert_into_db(table_name: str, data: list):

    rows = [item.model_dump() for item in data]

    cols = ", ".join(rows[0].keys())
    placeholders = ", ".join(['%s'] * len(rows[0]))
    q = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    values = [tuple(row.values()) for row in rows]
    conn = make_connection()
    cursor = conn.cursor()
    cursor.executemany(q, values)
    conn.commit()