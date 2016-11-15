from tkinter import *
from PIL import Image, ImageTk
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
'''
'''
root = Tk()

def printName(event):
	print("Hi, MAKE AMERICA GREAT AGAIN")

#button_1 = Button(root, text="America", command=printName)
button_1 = Button(root, text="America")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()
'''
'''
root = Tk()

def leftClick(event):
	print("left")

def rightClick(event):
	print("right")
def middleClick():
	print("Middle!!!")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)

frame.pack()

root.mainloop()
'''


'''
class LiamsButtons:
	def __init__(self, master):
		frame=Frame(master)
		frame.pack()

		self.printButton = Button(frame, text="Message", command=self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame, text="Quit", command=frame.quit)
		self.quitButton.pack(side=LEFT)
	def printMessage(self):
		print("Worky!")

root = Tk()
b = LiamsButtons(root)
root.mainloop()
'''

root = Tk()

buttonforimageA = Button(root, text = "Better")
buttonforimageB = Button(root, text = "Better")



imageFileA = Image.open("rain.jpg")
imageFileB = Image.open("darth.jpg")
photoA = ImageTk.PhotoImage(imageFileA)
photoB = ImageTk.PhotoImage(imageFileB)

imageA = Label(root, image=photoA)
imageB = Label(root, image=photoB)
imageA.image = photoA
imageB.image = photoB

imageA.grid(row=0,column=0)
imageB.grid(row=0,column=1)
buttonforimageA.grid(row=1,column=0)
buttonforimageB.grid(row=1,column=1)



root.mainloop()