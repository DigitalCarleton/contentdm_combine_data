"""
	rm_special_chars.py

	Usage: rm_special_chars.rm(<filename.extension>)
	To add or change replacement characters, edit chars_to_replace.csv 
    Edit CHARS_TO_REPLACE to match the location of your file.

	Input:  Text, CSV, HTML, etc., file with undesirable special characters
	Output: <filename><.extension> where the special characters have
	been replaced (replaces the old file).
"""

import csv, sys

# between directories, use:
# Windows:  \
# Mac/Unix: /
CHARS_TO_REPLACE = 'C:\Users\me\chars_to_replace.csv'

def rm(fname):

	# opens the text file that needs fixing
	f = open(fname)
	text = f.read()

	# splits file name into name and extension to help name the output file
	fileinfo = fname.split('.',1)
	output_fname = fileinfo[0] + '.' + fileinfo[1]
	output = open(output_fname, 'w')

	replacements = 0
	reader = csv.reader(open(CHARS_TO_REPLACE))
	# skips header row
	reader.next()
	# checks for each invalid character and replaces it if found
	for char in reader:
		if char[0] in text:
			text = text.replace(char[0],char[1])
			replacements+=1

	output.write(text)
	print "\n", replacements , "replacement(s) made." , output_fname, "has been overwritten.",
	f.close()
