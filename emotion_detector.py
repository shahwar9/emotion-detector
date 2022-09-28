import cv2
from deepface import DeepFace
import numpy as np  #this will be used later in the process

imgpath = "boy_sad.jpeg"  #put the image where this file is located and put its name here
image = cv2.imread(imgpath)

analyze = DeepFace.analyze(image, actions=['emotion'])  
print(analyze)