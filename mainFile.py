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

def makeResultsFile():
	with open("Results.txt", "w") as f:
		tempEloForWriting = str(defaultELO)
		for filename in os.listdir():
			f.write(filename + ',' + tempEloForWriting + ',0,0' + '\n')
		#for line in ("Results.text", "w")
		#	if line = "mainFile.py,1000" or "Results.text,1000"
		# At some point i need to get rid of the first two lines of output.. right now, sloppy

def expectedELO(A, B):
    """
    Calculate expected score of A in a match against B

    :param A: Elo rating for player A
    :param B: Elo rating for player B
    """
    return 1 / (1 + 10 ** ((B - A) / 400))


def eloCalc(old, exp, score, k=32):
    """
    Calculate the new Elo rating for a player

    :param old: The previous Elo rating
    :param exp: The expected score for this match
    :param score: The actual score for this match
    :param k: The k-factor for Elo (default: 32)
    """
    return old + k * (score - exp)






if __name__ == '__main__':

	#So, this checks if, in the current folder, there is a results file
	if not os.path.exists(currentPath + "\Results.txt"):
		print("I made you a new Results file! NOW DO YOU LOVE ME DADDY!?")
		makeResultsFile()
	
	ImageA = 1200
	ImageB = 1000

	exp = expectedELO(ImageA, ImageB)

	print (round(eloCalc(ImageA, exp, 5), 5))
	print (round(eloCalc(ImageB, exp, 5), 5))