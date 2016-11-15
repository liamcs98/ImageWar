#William Smith
#Goal: Use ELO math to rank images in a directory
#TO FUCKING DO, LEARN ABOUT ARRAYS... ShIT MAKES NO SENSE
#
import PIL
from PIL import Image, ImageFilter, ImageTk
import os
import shutil
from random import randint
from tkinter import *

defaultELO = 1000 #I have no idea what a good elo is...so meh
currentPath = os.path.dirname(os.path.abspath(__file__))
data = []
NumberOfFiles = 0
ImageANum = 0 
ImageBNum = 0 
ImageAElo = 0
ImagebElo = 0
imageA = 0 
imageB = 0


def makeResultsFile():
	with open("Results.txt", "w") as f:
		for filename in os.listdir():
			ispng = filename.find(".png") != -1
			isjpg = filename.find(".jpg") != -1
			isgif = filename.find(".gif") != -1
			isjpeg = filename.find(".jpeg") != -1
			iswebm = filename.find(".webm") != -1
			#Above whitelists the above filetypes
			isvalid = ispng or isjpg or isgif or isjpeg or iswebm

			if isvalid:
				tempEloForWriting = str(randint(0,2000))
				f.write(filename + ',' + tempEloForWriting + ',0,0\n')
			else:
				print(filename + " Is not A FUCKING SUPPORTED FILE TYPE....(Ignored)")
		#for line in ("Results.text", "w")
		#	if line = "mainFile.py,1000" or "Results.text,1000"
		# At some point i need to get rid of the first two lines of output.. right now, sloppy
def eloCalc(ELOA, ELOB, winner, k=32):
	#This Funtion that gets the ELO of the two competitors, + which one wins, does the meth, 
	#then returns NewEloA, NewEloB
  
	if winner == "draw":
		SOne = .5
		STwo = .5
	elif winner == "ImageA":
		SOne = 1
		STwo = 0
	elif winner == "ImageB":
		SOne = 0
		STwo = 1

	ROne = 10**(int(ELOA)/400)
	RTwo = 10**(int(ELOB)/400)

	EOne = ROne / (ROne + RTwo)
	ETwo = RTwo / (ROne + RTwo)

	print(ELOA + k * (SOne - EOne))
	print(ELOB + k * (STwo - ETwo))

	return ELOA + k * (SOne - EOne), ELOB + k * (STwo - ETwo)
def parseResultsFileToData():
	global data, NumberOfFiles
	with open("Results.txt", "r") as f:
		# So this fucking line here has a lot going on. Reminder to future me to try to understand it better. 
		#data.append([[filename, int(elo), int(wins), int(losses)] for filename, elo, wins, losses in [[element.strip() for element in line.split(',')]]][0])
		data = [[filename, int(elo), int(wins), int(losses)] for filename, elo, wins, losses in [[element.strip() for element in line] for line in [line.split(',') for line in f]]]	
		NumberOfFiles = len(data)
def updateResultsFile():
	with open("Results.txt", "w") as f:
		for filename, elo, wins, losses in data:
			f.write("%s,%i,%i,%i \n" % (filename, elo, wins, losses))
	print("Updated Results File.")
def randomImages():
	global ImageANum, ImageBNum
	#Check to make sure that I have at least two files. 
	if NumberOfFiles <= 1:
		print("Liam....number of files? Sigh")
		quit()

	ImageANum = int(randint(0,NumberOfFiles-1))
	ImageBNum = int(randint(0,NumberOfFiles-1))
	print("Random Images Selected.")

	while ImageANum == ImageBNum:
		ImageANum = randint(0,NumberOfFiles-1)
def uglyELOWinnerA(event):
	global ImageAElo, ImageBElo, imageA, imageB
	NewImageAElo, NewImageBElo = eloCalc(ImageAElo, ImageBElo, "ImageA")
	print("WinnerA")

	NewImageAElo = round(int(NewImageAElo), 5)
	NewImageBElo = round(int(NewImageBElo), 5)

	data[ImageANum][1] = NewImageAElo
	data[ImageBNum][1] = NewImageBElo

	updateResultsFile()
	randomImages()

	ImageAElo = data[ImageANum][1]
	ImageBElo = data[ImageBNum][1]

	buttonforimageA = Button(root, text = "Better")
	buttonforimageB = Button(root, text = "Better")


	imageFileA = PIL.Image.open(data[ImageANum][0])
	imageFileB = PIL.Image.open(data[ImageBNum][0])
	imageFileA = imageFileA.resize((300,300))
	imageFileB = imageFileB.resize((300,300))
	photoA = PIL.ImageTk.PhotoImage(imageFileA)
	photoB = PIL.ImageTk.PhotoImage(imageFileB)

	imageA = Label(root, image=photoA)
	imageB = Label(root, image=photoB)
	imageA.image = photoA
	imageB.image = photoB

	buttonforimageA.bind("<Button-1>", uglyELOWinnerA)
	buttonforimageB.bind("<Button-1>", uglyELOWinnerB)

	imageA.grid(row=0,column=0)
	imageB.grid(row=0,column=1)
	buttonforimageA.grid(row=1,column=0)
	buttonforimageB.grid(row=1,column=1)
def uglyELOWinnerB(event):
	global ImageAElo, ImageBElo, imageA, imageB
	NewImageAElo, NewImageBElo = eloCalc(ImageAElo, ImageBElo, "ImageB")
	print("WinnerB")

	NewImageAElo = round(int(NewImageAElo), 5)
	NewImageBElo = round(int(NewImageBElo), 5)

	data[ImageANum][1] = NewImageAElo
	data[ImageBNum][1] = NewImageBElo

	updateResultsFile()
	randomImages()

	ImageAElo = data[ImageANum][1]
	ImageBElo = data[ImageBNum][1]

	buttonforimageA = Button(root, text = "Better")
	buttonforimageB = Button(root, text = "Better")


	imageFileA = PIL.Image.open(data[ImageANum][0])
	imageFileB = PIL.Image.open(data[ImageBNum][0])
	imageFileA = imageFileA.resize((300,300))
	imageFileB = imageFileB.resize((300,300))
	photoA = PIL.ImageTk.PhotoImage(imageFileA)
	photoB = PIL.ImageTk.PhotoImage(imageFileB)

	imageA = Label(root, image=photoA)
	imageB = Label(root, image=photoB)
	imageA.image = photoA
	imageB.image = photoB

	buttonforimageA.bind("<Button-1>", uglyELOWinnerA)
	buttonforimageB.bind("<Button-1>", uglyELOWinnerB)

	imageA.grid(row=0,column=0)
	imageB.grid(row=0,column=1)
	buttonforimageA.grid(row=1,column=0)
	buttonforimageB.grid(row=1,column=1)


if __name__ == '__main__':


	#So, this checks if, in the current folder, there is a results file
	if not os.path.exists(currentPath + "\Results.txt"):
		print("I made you a new Results file! NOW DO YOU LOVE ME DADDY!?")
		makeResultsFile()
	
	parseResultsFileToData()
	randomImages()




	ImageAElo = data[ImageANum][1]
	ImageBElo = data[ImageBNum][1]
###############

	root = Tk()

	buttonforimageA = Button(root, text = "Better")
	buttonforimageB = Button(root, text = "Better")


	imageFileA = PIL.Image.open(data[ImageANum][0])
	imageFileB = PIL.Image.open(data[ImageBNum][0])
	imageFileA = imageFileA.resize((300,300))
	imageFileB = imageFileB.resize((300,300))
	photoA = PIL.ImageTk.PhotoImage(imageFileA)
	photoB = PIL.ImageTk.PhotoImage(imageFileB)

	imageA = Label(root, image=photoA)
	imageB = Label(root, image=photoB)
	imageA.image = photoA
	imageB.image = photoB

	#MOTHERFUCKING CAPTICAL "B" Also, this code call the funtion of the winner, and should (hypothetically) allow for the 
	#program to be a loop... right now there is no refresh of the picture. 
	buttonforimageA.bind("<Button-1>", uglyELOWinnerA)
	buttonforimageB.bind("<Button-1>", uglyELOWinnerB)

	imageA.grid(row=0,column=0)
	imageB.grid(row=0,column=1)
	buttonforimageA.grid(row=1,column=0)
	buttonforimageB.grid(row=1,column=1)



	root.mainloop()

#################



