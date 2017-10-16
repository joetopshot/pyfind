# pyfind
Python version of the *NIX find command

The original version of this file was created by Mihalis Tsoukalos
in an article called "Python: Write your own find" published in the 
May, 2017 issue of Linux Format magazine.

That version of the program worked nicely as is but didn't allow for
entering regular expressions for files and/or directories that were
being searched.

Note that this version of pyFind uses regular expressions so if you
want to find all files that end in mm execute the following line:
	pyFind.py . ".*mm$"
	
Without the '$' at the end you would get all files that contain 
the letters 'mm'.  

For all directories that start with 'freeplane', use
the following command:
	pyFind.py . "^freeplane.*" -d
	
