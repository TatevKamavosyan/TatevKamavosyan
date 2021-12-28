import mysql.connector
from mysql.connector  import Error

def create_connection(host_name,user_name,user_password):
    connection=None
    try:
        connection=mysql.connector.connect(
            host-host_name,
            user=user_name,
            passwd=user_password
            )
        print("Conection to MYSQL DB successful")
    except Error as e:
        print(f"The error '{e}' occured")
    return connection
def create_database(connection,query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        print("Database creaded successful")
    except Error as e:
        print(f"The error '{e}' occured")

connection=create_connection("localhost","root","")
create_database_query="CREATE DATABASE sm_app_2"
create_database(connection,create_database_query)
