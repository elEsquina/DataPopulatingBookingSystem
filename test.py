import mysql.connector

host = "localhost"
port = 3306
user = "root"
password = "avengetech7"
dbname = "project2"

try:
    con = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=dbname,
        port=port
    )
    if con.is_connected():
        print("Connected to the database")
    cursor = con.cursor()

    populate(cursor)

    con.commit()
    cursor.close()



except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'con' in locals() and con.is_connected():
        con.close()
        print("Connection closed")
