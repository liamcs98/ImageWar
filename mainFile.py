#William Smith
#Goal: Use ELO math to rank images in a directory
#TO FUCKING DO, LEARN ABOUT ARRAYS... ShIT MAKES NO SENSE
#
from PIL import Image, ImageFilter
import os
import shutil
from random import randint
from tkinter import *

#For later
#print(randint(0,9))

defaultELO = 1000 #I have no idea what a good elo is...so meh
currentPath = os.path.dirname(os.path.abspath(__file__))



def makeResultsFile():
	with open("Results.txt", "w") as f:
		
		for filename in os.listdir():
			tempEloForWriting = str(randint(0,2000))
			f.write(filename + ',' + tempEloForWriting + ',0,0\n')
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

    return ROne + k * (SOne - EOne), RTwo + k * (STwo - ETwo)
  

if __name__ == '__main__':
	data = []
	NumberOfFiles = 0

	#So, this checks if, in the current folder, there is a results file
	if not os.path.exists(currentPath + "\Results.txt"):
		print("I made you a new Results file! NOW DO YOU LOVE ME DADDY!?")
		makeResultsFile()

	with open("Results.txt", "r") as f:
		for line in f:
			# So this fucking line here has a lot going on. Reminder to future me to try to understand it better. 
			data.append([[filename, int(elo), int(wins), int(losses)] for filename, elo, wins, losses in [[element.strip() for element in line.split(',')]]][0])
			
			
			NumberOfFiles += 1
	ImageANum = int(randint(0,NumberOfFiles-1))
	ImageBNum = int(randint(0,NumberOfFiles-1))

	if ImageANum == ImageBNum:
		ImageANum = randint(0,NumberOfFiles-1)

	print(data)
	ImageAElo = data[ImageANum][1]
	ImageBElo = data[ImageBNum][1]
	winner = "ImageA"

	NewImageAElo, NewImageBElo = eloCalc(ImageAElo, ImageBElo, winner)

	NewImageAElo = round(int(NewImageAElo), 5)
	NewImageBElo = round(int(NewImageBElo), 5)

	data[ImageANum][1] = NewImageAElo
	data[ImageBNum][1] = NewImageBElo

	with open("Results.txt", "w") as f:
		for filename, elo, wins, losses in data:
			f.write("%s,%i,%i,%i \n" % (filename, elo, wins, losses))



