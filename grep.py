import re
import string
import sys


def countpatterninfile():
    regular_expression = input("Enter a regular expression: ")

    file_name = "mbox-long.txt"
    fhand = open(file_name)
    re_count = 0

    for line in fhand:
        #line = line.rstrip()
        if re.findall(regular_expression, line):
            re_count += 1
    
    print (f'mbox.txt had {re_count} lines that matched {regular_expression}')
        


if __name__ == '__main__':
    # this is called a main method
    # This is another way of telling python THIS IS WHERE YOU SHOULD START RUNNING
    # When this is included, python will begin with the code in this block first
    countpatterninfile()