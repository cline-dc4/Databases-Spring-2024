from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        print(connection)

        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES;")
        for x in cursor:
            print(x)
except Error as e:
    print(e)
