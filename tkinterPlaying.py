from tkinter import *

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