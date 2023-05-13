#When dealing with older systems that require you to upload images, such as defect tracking applications or expense management solutions, 
#it seems like they all accept JPEG images but rarely accept newer formats, such as PNG or HEIC.
#To resolve this issue, here’s a quick utility that will take the input file and convert it to a .jpg version using the same base name.

import os
import sys
from PIL import Image

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        im = Image.open(sys.argv[1])
        target_name = sys.argv[1] + ".jpg"
        rgb_im = im.convert('RGB')
        rgb_im.save(target_name)
        print("Saved as " + target_name)
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: convert2jpg.py <file>")
