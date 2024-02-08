"""
Aim: this script counts the number of lines in standard input
Input: strings from the command line
Output: count the number of lines
Author: J. Araiku
"""

import sys

count = 0
for line in sys.stdin:
	count += 1

print(count, "lines in standard input")
