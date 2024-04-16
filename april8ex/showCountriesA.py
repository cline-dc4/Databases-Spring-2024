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
        cursor.execute("SELECT name \
                    FROM world.country \
                    WHERE name LIKE 'A%';")
        for x in cursor:
            print(x)
except Error as e:
    print(e)
