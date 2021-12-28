import mysql.connector
from mysql.connector  import Error

def create_connection(host_name,user_name,user_password,db_name):
    connection=None
    try:
        connection=mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
            )
        print("Conection to MYSQL DB successful")
    except Error as e:
        print(f"The error '{e}' occured")
    return connection


connection=create_connection("localhost","root","","sm_app")
