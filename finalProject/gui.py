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
                messageString = ''
                for x in cursor:
                    messageString = messageString + x[0] + '\n'
                #add the price to the beginning of the string
                queryPrice = 'SELECT price FROM dcbcdb.CoffeeDrink WHERE drink_name = "' + dropdownSelected.get() + '";'
                cursor.execute(queryPrice)
                for x in cursor:
                    messageString = 'Price: $' + str(x[0]) + '\n' + messageString
                #show information
                messagebox.showinfo(title = 'Coffee Info', message = messageString)
                coffeeWindow.destroy()
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
                    coffeeAddWindow.destroy()
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
                    #dropdown menu for ingredient names
                    coffeeDropdown = OptionMenu(addIngredientGui, dropdownSelected, *options)
                    l = Label(master=addIngredientGui, text='Select an ingredient you would like to\nadd and click the "add" button.\nOnce all ingredients are added, click "done" to save.')
                    l.place(x=50, y=15)
                    coffeeDropdown.place(x=100, y=75)

                    #buttons
                    #function for the done button
                    def doneButtonFunction():
                        connection.commit()
                        addIngredientGui.destroy()

                    #function for the add button
                    def addButtonFunction():
                        #query ingredient_id from ingredient_name
                        getIngredientIdQuery = "SELECT ingredient_id FROM dcbcdb.CoffeeIngredient WHERE ingredient_name = '" + dropdownSelected.get() + "';"
                        print(getIngredientIdQuery)
                        cursor.execute(getIngredientIdQuery)
                        for x in cursor:
                            ingredient_id = x[0]
                        try:
                            #add the drink_id and ingredient_id into IngredientList
                            addIngredientQuery="INSERT INTO dcbcdb.IngredientList VALUES(" + str(drink_id) + ",  " + str(ingredient_id) + ");"
                            cursor.execute(addIngredientQuery)
                        except Error as e:
                            messagebox.showerror(title = 'Error', text = 'Error when adding ingredients into database.\n')
                    #buttons for the functions above
                    doneButton = Button(master = addIngredientGui, text = 'done', command = doneButtonFunction)
                    doneButton.place(x = 120, y = 130)
                    addButton = Button(master = addIngredientGui, text = 'add', command = addButtonFunction)
                    addButton.place(x = 160, y = 130)
                    addIngredientGui.mainloop()
                ingredientAdd()
            coffeeAddWindow.mainloop()

#######################################################################################################

        def coffeeDeleteGui():
            coffeeDeleteWindow = Tk()
            coffeeDeleteWindow.geometry('300x300')

            #label with instructions
            l = Label(master = coffeeDeleteWindow, 
                      text = 'Use the dropdown to select drink to delete. \
                      \n Click the delete button to stage the deletion. \
                      \n Use the commit button to save the changes.')
            l.pack()
            #dropdown for drinks
            options = []
            #list drink names and set options for the dropdown menu.
            cursor.execute('SELECT drink_name FROM dcbcdb.CoffeeDrink;')
            for x in cursor:
                options.append(x[0])
            #set default value for dropdown
            dropdownSelected = StringVar(master=coffeeDeleteWindow)
            dropdownSelected.set(options[0])
            #dropdown menu for drink names
            coffeeDropdown = OptionMenu(coffeeDeleteWindow, dropdownSelected, *options)
            coffeeDropdown.pack()

            #function to delete the drink and IngredientList items that is called by deleteButton
            def deleteButtonFunction():
                #get drink_id from the drink_name
                drinkIdQuery = "SELECT drink_id FROM dcbcdb.CoffeeDrink WHERE drink_name = '" + dropdownSelected.get() + "';"
                cursor.execute(drinkIdQuery)
                for x in cursor:
                    drink_id = x[0]
                #delete from IngredientList using drink_id
                IngredientListDeleteQuery = "DELETE FROM dcbcdb.IngredientList WHERE drink_id = " + str(drink_id) + ";"
                cursor.execute(IngredientListDeleteQuery)

                #delete from CoffeeDrink using drink_id
                CoffeeDrinkDeleteQuery = "DELETE FROM dcbcdb.CoffeeDrink WHERE drink_id = " + str(drink_id) + ";"
                cursor.execute(CoffeeDrinkDeleteQuery)
            
            #function to commit changes made by the delete button
            def commitButtonFunction():
                connection.commit()
                coffeeDeleteWindow.destroy()
            deleteButton = Button(master = coffeeDeleteWindow, text = 'Delete', command = deleteButtonFunction)
            commitButton = Button(master = coffeeDeleteWindow, text = 'Commit changes', command = commitButtonFunction)
            deleteButton.pack()
            commitButton.pack()
            coffeeDeleteWindow.mainloop()

#######################################################################################################

        #Gui for updating the price of a drink(and seeing the current price)
        def priceUpdateGui():
            priceUpdateWindow = Tk()
            priceUpdateWindow.geometry('300x300')
            
            #form to add the new price
        
            priceForm = Entry(master = priceUpdateWindow, width = 20)
            priceForm.pack()
            #label with instructions
            l = Label(master = priceUpdateWindow, 
                      text = 'Use the form above to enter the new price. \
                      \n Use the dropdown to select drink to update. \
                      \n Click the update button to open the next menu.')
            l.pack()

            #dropdown for drinks
            options = []
            #list drink names with prices and set options for the dropdown menu.
            cursor.execute('SELECT drink_name, price FROM dcbcdb.CoffeeDrink;')
            for x in cursor:
                options.append(x[0])
            #set default value for dropdown
            dropdownSelected = StringVar(master=priceUpdateWindow)
            dropdownSelected.set(options[0])
            #dropdown menu for drink names
            coffeeDropdown = OptionMenu(priceUpdateWindow, dropdownSelected, *options)
            coffeeDropdown.pack()

            #function used by the update button to run a query to update the price for the selected drink
            def updatePrice():
                cursor.execute('SELECT drink_id FROM dcbcdb.CoffeeDrink WHERE drink_name = "' + dropdownSelected.get() + '";')
                for x in cursor:
                    drink_id = x[0]
                print(drink_id)
                updatePriceQuery = 'UPDATE dcbcdb.CoffeeDrink \
                                    SET price = ' + priceForm.get() + ' \
                                    WHERE drink_id = ' + str(drink_id) + ';'
                cursor.execute(updatePriceQuery)

            #function used by the commit button to push changes to the database
            def commitUpdate():
                connection.commit()
                priceUpdateWindow.destroy()
    
            #button to stage the price change
            updateButton = Button(priceUpdateWindow, text = 'Select', command = lambda: updatePrice())
            updateButton.pack()
            #button to commit the changes
            commitButton = Button(priceUpdateWindow, text = 'Commit', command = lambda: commitUpdate())
            commitButton.pack()

            priceUpdateWindow.mainloop()

#######################################################################################################

        #home gui
        mainWindow = Tk()
        mainWindow.title('DCBCDB')
        mainWindow.geometry('500x300')
        coffeeInfoButton = Button(mainWindow, text = 'Drink Info', command = lambda: coffeeInfoGui())
        coffeeInfoButton.place(x = 71, y = 50)
        coffeeDeleteButton = Button(mainWindow, text = 'Delete a drink', command = lambda: coffeeDeleteGui())
        coffeeDeleteButton.place(x = 136, y = 50)
        coffeeAddButton = Button(mainWindow, text = 'Add new drink', command = lambda: coffeeAddGui()) 
        coffeeAddButton.place(x=220,y=50)
        priceEditButton = Button(mainWindow, text = 'Update price', command = lambda: priceUpdateGui())
        priceEditButton.place(x=310, y = 50)
        mainWindow.mainloop()

except Error as e:
    print(e)
