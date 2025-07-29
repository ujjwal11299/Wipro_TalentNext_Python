#Through command line arguments, three strings separated by space are given.
#Each string is a series of numbers separated by hyphen (-).

import sys

like = set(sys.argv[1].split('-'))
dislike = set(sys.argv[2].split('-'))
given = sys.argv[3].split('-')

happiness = 0

for num in given:
    if num in like:
        happiness += 1
    elif num in dislike:
        happiness -= 1

print(happiness)
