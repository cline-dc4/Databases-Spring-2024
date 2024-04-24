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
except Error as e:
    print(e)

cursor = connection.cursor()

#testButtonFunction
def testButtonFunction(string):
    string ='[' + string + ']'
    msg=messagebox.showinfo(testEntry.get(), string)
#home gui
testWindow = Tk()
testWindow.title('DCBCDB')
testWindow.geometry('500x300')


#coffee gui
def coffeeGui():
    coffeeWindow = Tk()
    coffeeWindow.title('DCBCDB: Coffee')
    coffeeWindow.geometry('500x300')

    #dropdown for drinks
    options = []
    cursor.execute('SELECT drink_name FROM dcbcdb.CoffeeDrink;')
    for x in cursor:
        options.append(x)
    coffeeDropdown = OptionMenu(coffeeWindow, options)
    coffeeDropdown.pack
    coffeeWindow.mainloop()

coffeeGui()
buttonString ="test: please click here:"
testEntry = Entry(width = 50)
testEntry.place(x = 50, y = 80)
testButton = Button(testWindow, text = buttonString, command = lambda: testButtonFunction(buttonString))
testButton.place(x = 50, y = 50)
testWindow.mainloop()