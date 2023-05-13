#This script will read a file and either pass the file as being a valid JSON file, or die a horrible death. 
#But for all practical reasons, it tells me if the error is in the file or the program that I am trying to load the file into.

import os
import sys
import json

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("Validate JSON!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: checkjson.py <file>")
