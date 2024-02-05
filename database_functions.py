import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="A.m.13015",
        database="store"
    )

def execute_query(query):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
