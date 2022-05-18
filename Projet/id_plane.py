 #importing Our dependencies

import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np


IMAGE_PATH = 'reg2.jpg'
#getting data from our functions

reader = easyocr.Reader(['en'],gpu=True)
#in the upper command we have setted the language to english and
#Enabled the GPU for more accurate and faster results and since our machine support one why not use it

########################################
##### Getting the result

result = reader.readtext(IMAGE_PATH)
print(result)
