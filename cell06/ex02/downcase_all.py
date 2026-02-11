#!/usr/bin/python3
import sys

def downcase_it(str):
    return str.lower()
if len(sys.argv) > 1:
        for n in sys.argv:
            print(downcase_it(n))
else:
        print("none")
# ./downcase_all.py
#./downcase_all.py "HELLO WORLD" "I understood Arrays well!"