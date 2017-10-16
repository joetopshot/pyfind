#!/usr/bin/python

import os
import sys

def find(directory, filename, dirOnly, fileOnly):
	if (dirOnly == 0 and fileOnly == 0):
		dirOnly = 1;
		fileOnly = 1;

	for root, dirs, files in os.walk(directory):
		if dirOnly == 1:
			if os.path.basename(os.path.normpath((root))) == filename:
				print(root)
		for file in files:
			pathname = os.path.join(root, file)
			if os.path.exists(pathname):
				if (fileOnly == 1):
					if file == filename:
						print(pathname)

def main():
	dirOnly = 0;
	fileOnly = 0;
	if len(sys.argv) == 3:
		directory = str(sys.argv[1])
		filename = str(sys.argv[2])
	elif len(sys.argv) == 4:
		directory = str(sys.argv[1])
		filename = str(sys.argv[2])
		option1 = str(sys.argv[3])
		if option1 == "-d":
			dirOnly = 1;
		if option1 == "-f":
			fileOnly = 1;
	elif len(sys.argv) >= 5:
		directory = str(sys.argv[1])
		filename = str(sys.argv[2])
		option1 = str(sys.argv[3])
		option2 = str(sys.argv[4])
		if option1 == "-d" or option2 == "-d":
			dirOnly = 1;
		if option1 == "-f" or option2 == "-f":
			fileOnly = 1;
	else:
		print('Usage: ', sys.argv[0], 'directory filename[-df]')
		sys.exit(0)
	
	#if the given path exists do your job
	if os.path.isdir(directory):
		find(directory, filename, dirOnly, fileOnly)
	else:
		print('Directory ', directory, ' does not exist!')

if __name__ == '__main__':
	main()
else:
	print("this is a standalone not a module!")

