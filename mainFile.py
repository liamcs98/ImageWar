#William Smith
#Goal: Use ELO math to rank images in a directory
#
#
from PIL import Image, ImageFilter
import os
import shutil


def makeResultsFile():
	with open("Results.txt", "w") as f:
		for filename in os.listdir():
			f.write(filename + '\n')





if __name__ == '__main__':
	makeResultsFile()
	