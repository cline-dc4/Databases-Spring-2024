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

            #Ingredient Checkboxes:
            #get the list of ingredient names
            getIngredientsQuery = "SELECT ingredient_name, ingredient_id FROM dcbcdb.CoffeeIngredient"
            ingredientList = []
            ingredientIdList = []
            cursor.execute(getIngredientsQuery)
            #add the checkbutton for each ingredient in the database
            for x in cursor:
                ingredientList.append(x[0])
            i = 0
            #list to hold the variables changed by checking and unchecking the boxes
            checkbuttonVariableList = []
            #create checkbuttons
            for name in ingredientList:
                #create ID list
                ingredientIdList.append(x[1])
                checkbuttonVariableList.append(Variable(value=0))
            for name in ingredientList:
                Checkbutton(coffeeAddWindow, variable = checkbuttonVariableList[i], text = name).place(x=50, y=90+(20*i))
                i = i + 1
                print(checkbuttonVariableList)

            #button to run add function
            runInsertButton = Button(coffeeAddWindow, text = 'Add drink', command = lambda: coffeeAdd())
            runInsertButton.place(x=350, y=50)

            #function for the coffeeAddButton
            def coffeeAdd():
                checkbuttonStateList = []
                for x in checkbuttonVariableList:
                    checkbuttonStateList.append(x.get())
                name = coffeeNameEntry.get()
                price = coffeePriceEntry.get()
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

                #add to the ingredient list using checkbuttons
                cursor.execute(DrinkIdSqlQuery)
                drink_id = 0
                i = 0
                #find the drink_id for the new drink name
                for x in cursor:
                    drink_id = x[0]
                print(checkbuttonStateList[1])
                for x in checkbuttonStateList:
                    print(x)
                    print(i)
                    print(checkbuttonStateList[i])
                    if (checkbuttonStateList[i] == 1):
                        #set up the query to add to IngredientList
                        addIngredientQuery = "INSERT INTO dcbcdb.IngredientList VALUES(" + str(drink_id) + " " + str(ingredientIdList[i].get()) + ")"
                        print(addIngredientQuery)
                        i = i + 1
                coffeeAddWindow.mainloop()

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
