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
        cursor.execute("UPDATE world.country \
                       SET world.country.HeadOfState = 'Condoleezza Rice' \
                       WHERE code = 'USA';")
        connection.commit()
        cursor.execute("SELECT * FROM world.country WHERE code = 'USA';")
        for x in cursor:
            print(x)
except Error as e:
    print(e)
