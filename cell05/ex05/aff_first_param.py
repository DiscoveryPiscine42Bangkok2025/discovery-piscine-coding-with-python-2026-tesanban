#!/usr/bin/python3
import sys
try:
    if sys.argv[1]:
        print(sys.argv[1])
except:
    print("none")

#./aff_first_param.py
#./aff_first_param.py "Code Ninja" "Numerique" "42" | cat -e