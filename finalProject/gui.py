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

#######################################################################################################

        #coffee information gui
        def coffeeInfoGui():
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

#######################################################################################################

        #coffee drink adding gui
        def coffeeAddGui():
            coffeeAddWindow = Tk()
            coffeeAddWindow.geometry('500x300')
            #labels and entries
            coffeeNameEntry = Entry(coffeeAddWindow, width = 20)
            coffeeNameLabel = Label(coffeeAddWindow, text = 'Drink name:')
            coffeePriceEntry = Entry(coffeeAddWindow, width = 20)
            coffeePriceLabel = Label(coffeeAddWindow, text = 'Drink price:')
            #place them
            coffeeNameLabel.place(x=50,y=20)
            coffeeNameEntry.place(x=120,y=20)
            coffeePriceLabel.place(x=50,y=70)
            coffeePriceEntry.place(x=120,y=70)
            #button to run add function
            runInsertButton = Button(coffeeAddWindow, text = 'Add drink', command = lambda: coffeeAdd())
            runInsertButton.place(x=350, y=50)

            #function for the coffeeAddButton
            def coffeeAdd():
                name = coffeeNameEntry.get()
                print(name)
                price = coffeePriceEntry.get()
                print(price)
                #construct sql query to add a row
                drinkSqlQuery = "INSERT INTO dcbcdb.CoffeeDrink \
                            VALUES \
                                (0, '" + name + "', "+ price + ")"
                #construct sql query to get drink_id from name
                DrinkIdSqlQuery = "SELECT drink_id FROM dcbcdb.CoffeeDrink WHERE drink_name = '" + name + "';" 
                #try except for input validation
                try: 
                    cursor.execute(drinkSqlQuery)
                #if sql throws an error create alert for user
                except Error as e:
                    messagebox.showerror(title = 'Input Error', message = 'Make sure that the price is valid (less than $99)\nNote that name must be less than 40 characters long')
                    print('exception thrown')

                #connection.commit()

                #open a new menu for IngredientList additions (use dropdown menus)
                def ingredientAdd():
                    addIngredientGui = Tk()
                    addIngredientGui.geometry('350x200')
                    #find the drink_id
                    cursor.execute(DrinkIdSqlQuery)
                    drink_id = 0
                    for x in cursor:
                        drink_id = x[0]

                    #variables for the dropdown menu
                    options = []
                    cursor.execute('SELECT ingredient_name FROM dcbcdb.CoffeeIngredient;')
                    for x in cursor:
                        options.append(x[0])
                    #set default value for dropdown
                    dropdownSelected = StringVar(master=addIngredientGui)
                    dropdownSelected.set(options[0])
                    #dropdown menu for drink names
                    coffeeDropdown = OptionMenu(addIngredientGui, dropdownSelected, *options)
                    l = Label(master=addIngredientGui, text='Select an ingredient you would like to\nadd and click the "add" button.\nOnce all ingredients are added, click "done".')
                    l.place(x=50, y=15)
                    coffeeDropdown.place(x=100, y=75)

                    #buttons
                    #bool to ensure at least 1 ingredient has been added
                    addButtonClick = False
                    doneButton = Button(text = 'done', command = doneButtonFunction())
                    addButton = Button(text = 'add', command = addButtonFunction())
                    #function for the done button
                    def doneButtonFunction():
                        if not addButtonClick:
                            messagebox.showerror(title = 'Error', message = 'No ingredients have been added')
                        else:
                            addIngredientGui.destroy()

                    #function for the add button
                    def addButtonFunction():
                        queryString="INSERT INTO IngredientList VALUES(" + drink_id + ",  " + dropdownSelected.get() + ")"
                        print(queryString)
                    #TODO: include compatability for a dropdown menu of ingredients(when button pressed, add a row with drink_id and ingredient_id for selected ingredient)


                    addIngredientGui.mainloop()
                ingredientAdd()
            coffeeAddWindow.mainloop()

#######################################################################################################


        #home gui
        mainWindow = Tk()
        mainWindow.title('DCBCDB')
        mainWindow.geometry('500x300')
        coffeeInfoButton = Button(mainWindow, text = 'Coffee', command = lambda: coffeeInfoGui())
        coffeeInfoButton.place(x = 50, y = 50)
        coffeeAddButton = Button(mainWindow, text = 'Add new drink', command = lambda: coffeeAddGui()) 
        coffeeAddButton.place(x=200,y=50)
        mainWindow.mainloop()

except Error as e:
    print(e)
