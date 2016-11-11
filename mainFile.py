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

currentPath = os.path.dirname(os.path.abspath(__file__))

def makeResultsFile():
	with open("Results.txt", "w") as f:
		for filename in os.listdir():
			f.write(filename + '\n')





if __name__ == '__main__':

	#So, this checks if, in the current folder, there is a results file
	if not os.path.exists(currentPath + "Results.txt"):
		makeResultsFile()
	