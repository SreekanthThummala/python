#Kubernetes is difficult enough without having YAML fail to parse. 
#This utility is a way to validate that the YAML is valid. Use it before ripping apart the program you are trying to load it into.

import os
import sys
import yaml

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        yaml.safe_load(file.read())
        file.close()
        print("Validate YAML!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: checkyaml.py <file>")
