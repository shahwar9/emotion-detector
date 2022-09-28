import cv2
import numpy as np
from deepface import DeepFace 

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    #making a try and except condition in case of any errors
    try:
        analyze = DeepFace.analyze(frame,actions=['emotion'])  #same thing is happing here as the previous example, we are using the analyze class from deepface and using ‘frame’ as input
        print(analyze['dominant_emotion'])  #here we will only go print out the dominant emotion also explained in the previous example
    except:
        print("no face")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()