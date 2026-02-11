#!/usr/bin/python3
import sys

if len(sys.argv) < 3:
    print("none")
else:
    for n in sys.argv:
        print(n)

#./aff_rev_params.py | cat -e
# ./aff_rev_params.py "coucou" | cat -e
#./aff_rev_params.py "Python" "piscine" "hello" | cat -e