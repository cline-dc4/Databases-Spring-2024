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
                       SET world.country.population = 4598000, \
                       world.country.LifeExpectancy = 74.5 \
                       WHERE code = 'ARM'")
        connection.commit()
except Error as e:
    print(e)
