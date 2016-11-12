#William Smith
#Goal: Use ELO math to rank images in a directory
#
#
from PIL import Image, ImageFilter
import os
import shutil
from random import randint

#For later
#print(randint(0,9))

defaultELO = 1000 #I have no idea what a good elo is...so meh
currentPath = os.path.dirname(os.path.abspath(__file__))

data = []

def makeResultsFile():
	with open("Results.txt", "w") as f:
		tempEloForWriting = str(defaultELO)
		for filename in os.listdir():
			f.write(filename + ',' + tempEloForWriting + ',0,0' + '\n')
		#for line in ("Results.text", "w")
		#	if line = "mainFile.py,1000" or "Results.text,1000"
		# At some point i need to get rid of the first two lines of output.. right now, sloppy
def eloCalc(ELOA, ELOB, winner, k=32):
	#This Funtion that gets the ELO of the two competitors, + which one wins, does the meth, 
    #then returns NewEloA, New EloB
  
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

	#So, this checks if, in the current folder, there is a results file
	if not os.path.exists(currentPath + "\Results.txt"):
		print("I made you a new Results file! NOW DO YOU LOVE ME DADDY!?")
		makeResultsFile()

	with open("Results.txt", "r") as f:
		for line in f:
			data.append(line.split(','))
	print(data)

	
	ImageA = int(1200)
	ImageB = int(1000)
	winner = "ImageA"

	NewImageA, NewImageB = eloCalc(ImageA, ImageB, winner)

	print (round(NewImageA, 5))
	print (round(NewImageB, 5))