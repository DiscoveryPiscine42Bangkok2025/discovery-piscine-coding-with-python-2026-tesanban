#!/usr/bin/python3
import sys
try:
    if sys.argv[1]:
        print(sys.argv[1].lower())
except:
    print("none")

#./downcase_it.py | cat -e
#./downcase_it.py "LUCIOLE" | cat -e
# ./downcase_it.py 'This exercise is quite easy!' | cat -e