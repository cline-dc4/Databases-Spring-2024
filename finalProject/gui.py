from tkinter import *
from tkinter import messagebox
from getpass import getpass
from mysql.connector import connect, Error

#connect to MySQL
try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        print(connection)
        cursor = connection.cursor()

        #function for coffeeIngredientButton
        def coffeeIngredientButton():
            

        #coffee gui
        def coffeeGui():
            coffeeWindow = Tk()
            coffeeWindow.title('DCBCDB: Coffee')
            coffeeWindow.geometry('500x300')

            #dropdown for drinks
            options = []
            #list drink names and set options for the dropdown menu.
            cursor.execute('SELECT drink_name FROM dcbcdb.CoffeeDrink;')
            for x in cursor:
                options.append(x[0])
            default = StringVar(master=coffeeWindow)
            default.set(options[0])
            #dropdown menu for drink names
            coffeeDropdown = OptionMenu(coffeeWindow, default, *options)
            coffeeDropdown.place(x=50, y=50)
            coffeeButton

            coffeeWindow.mainloop()

        #home gui
        testWindow = Tk()
        testWindow.title('DCBCDB')
        testWindow.geometry('500x300')
        testButton = Button(testWindow, text = 'Coffee', command = coffeeGui)
        testButton.place(x = 50, y = 50)
        testWindow.mainloop()

except Error as e:
    print(e)
