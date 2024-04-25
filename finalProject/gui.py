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
            #set default value for dropdown
            dropdownSelected = StringVar(master=coffeeWindow)
            dropdownSelected.set(options[0])
            #dropdown menu for drink names
            coffeeDropdown = OptionMenu(coffeeWindow, dropdownSelected, *options)
            coffeeDropdown.place(x=50, y=50)

            #function for coffeeIngredientButton
            def coffeeIngredientButton():
                #query ingredients
                queryString = 'SELECT ci.ingredient_name \
                FROM dcbcdb.CoffeeDrink AS cd JOIN dcbcdb.IngredientList AS il JOIN dcbcdb.CoffeeIngredient AS ci \
                WHERE cd.drink_name = "' + dropdownSelected.get() + '" AND cd.drink_id = il.drink_id AND il.ingredient_id = ci.ingredient_id;'
                cursor.execute(queryString)
                #organize ingredients to be displayed
                messageString = ""
                for x in cursor:
                    messageString = messageString + x[0] + '\n'
                #show ingredients
                messagebox.showinfo(title = 'Coffee Ingredients', message = messageString)
            #ingredient button
            ingredientButton = Button(coffeeWindow, text = 'List Ingredients', command = lambda: coffeeIngredientButton())
            ingredientButton.place(x=200, y=50)

            coffeeWindow.mainloop()

        #home gui
        testWindow = Tk()
        testWindow.title('DCBCDB')
        testWindow.geometry('500x300')
        testButton = Button(testWindow, text = 'Coffee', command = lambda: coffeeGui())
        testButton.place(x = 50, y = 50)
        testWindow.mainloop()

except Error as e:
    print(e)
