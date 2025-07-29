#Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

import sys
print("File Name:", sys.argv[0])
print("Welcome Message:", sys.argv[1])
