def execute_query(connection,query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
create_users="""
INSERT INTO
users(name,age,gender,nationality)
VALUES
('James',25,'male',''USA)
"""
connection=create_connection()
execute_query(connection,create_users)
