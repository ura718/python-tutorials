#!/usr/bin/python

from sys import argv


# Accept file name from prompt
script, filename = argv


# Open create filehandle that opens the filename
txt = open(filename)


# Use filehandle to read the file
print txt.read()


# Read only one line
print txt.readline()


# Print List 
print txt.readlines()

