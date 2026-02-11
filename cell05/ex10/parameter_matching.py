#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    Para = sys.argv[1]
    u_input = input("What was the parameter? ")
    if u_input == Para:
        print("Good job!")
    else:
        print("Nope, sorry...")
        #./parameter_matching.py "Hello"