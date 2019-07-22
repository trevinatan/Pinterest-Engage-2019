import os
import sys
import re

# Problem Statement
#
# Write a program that takes a filename as input and prints the number of words in the file as output.
# Feel free to use the attached file as a dummy to test your solution or make your own test files.
# Estimate how much memory is used by your program (relative to the file size).

# Assumptions
# 1. File size - A file will be small enough to fit into secondary storage (a hard
# drive) but may be much larger than main memory.
# 2. The file is assumed to be in ASCII.
# 3. Words are delineated by one or more space characters, including whitespace, newline, carriage return and tab.


def wordcount(path):
    """Returns the number of individual words counted.
    NOTE: There is an iteration of 'lorem ipsum dolor...' missing a space after the punctuation.
    It is counted as two separate words despite the missing whitespace."""
    if not os.path.isfile(path):
        print("File path {} does not exist. Exiting...".format(path))
        sys.exit()

    with open(path) as fp:
        words = 0
        for line in fp:
            words += len(re.findall(r"[\w']+", line))
            # words += len(line.split())
        print(words)

wordcount('file.txt')  # 2000
wordcount('file_1.txt')  # 1108
wordcount('file_2.txt')  # 892
wordcount('file_3.txt')  # 374
wordcount('file_4.txt')  # 203
wordcount('file_5.txt')  # 171
wordcount('file_6.txt')  # 90
wordcount('file_7.txt')  # 45
wordcount('file_8.txt')  # 26
wordcount('file_9.txt')  # 18
wordcount('file_10.txt')  # 8
wordcount('tab.txt')  # 10
wordcount('newline.txt')  # 10
wordcount('return.txt')  # 10

# Stretch Goal
# Extend your program to handle a file with lines larger than main memory.
