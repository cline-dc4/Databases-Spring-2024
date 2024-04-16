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
        cursor.execute(
                        "INSERT INTO world.countrylanguage \
                        VALUES('USA', 'Ukrainian', 'F', 1.1 );"
                       )
        connection.commit()
        cursor.execute("SELECT * FROM world.countrylanguage WHERE countrycode = 'USA';")
        cursor.execute
        (
            "DELETE FROM world.countrylanguage \
            WHERE countryCode = 'USA' AND language = 'Ukrainian';"
        )
        connection.commit()
        cursor.execute("SELECT * FROM world.countrylanguage WHERE countrycode = 'USA';")
        for x in cursor:
            print(x)
except Error as e:
    print(e)
