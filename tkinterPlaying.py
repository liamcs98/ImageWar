from tkinter import *
'''
root = Tk()
topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(topframe, text="Winner", fg="red")
button2 = Button(topframe, text="Winner", fg="blue")
button3 = Button(topframe, text="Winner", fg="green")
button4 = Button(bottomframe, text="Winner", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop()
'''


root = Tk()

labelOne = Label(root, text="Name")
labelTwo = Label(root, text="Password")
entryOne = Entry(root)
entryTwo = Entry(root)

labelOne.grid(row=0, sticky=E)
labelTwo.grid(row=1, sticky=E)

entryOne.grid(row=0, column=1)
entryTwo.grid(row=1, column=1)

checkbox = Checkbutton(root, text="Keep me logged in")
checkbox.grid(row=3, columnspan=2)

root.mainloop()