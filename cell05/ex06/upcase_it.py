#!/usr/bin/python3
import sys
try:
    if sys.argv[1]:
        print(sys.argv[1].upper())
except:
    print("none")

#./upcase_it.py | cat -e
# ./upcase_it.py "initiation" | cat -e
#./upcase_it.py 'This exercise is quite easy!' | cat -e