import mysql.connector

def connect_to_database(host, user, password, database):
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        cursor = conn.cursor()
        return conn, cursor
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None
