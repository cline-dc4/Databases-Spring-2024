from tkinter import *
from tkinter import messagebox
from getpass import getpass
from mysql.connector import connect, Error

#connect to MySQL
#try:
#    with connect(
#        host="localhost",
#        user=input("Enter username: "),
#        password=getpass("Enter password: "),
#    ) as connection:
#        print(connection)
#except Error as e:
#    print(e)


#testButtonFunction
def testButtonFunction(string):
    string ='[' + string + ']'
    msg=messagebox.showinfo(testEntry.get(), string)
#home gui
testWindow = Tk()
testWindow.title('test')
testWindow.geometry('500x300')
label = Label(text = "proof of concept")
label.place(x = 50, y = 30)
buttonString ="test: please click here:"
testEntry = Entry(width = 50)
testEntry.place(x = 50, y = 80)
testButton = Button(testWindow, text = buttonString, command = lambda: testButtonFunction(buttonString))
testButton.place(x = 50, y = 50)
testWindow.mainloop()