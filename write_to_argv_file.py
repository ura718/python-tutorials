#!/usr/bin/python

from sys import argv


# Accept one option from user, stores it inside 'filename' variable.

script, filename = argv

# Open filename for writing even if it doesnt exists.

txt = open(filename, 'w')

# Erase all contents of file

txt.truncate()

# Write to file

message = "I wrote to this file"
txt.write(message)
txt.write("\n")
txt.write("end")
txt.write("\n")


# Close the file

txt.close()
