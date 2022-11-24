import cv2
from deepface import DeepFace
import numpy as np  #this will be used later in the process
import argparse 
from pprint import pprint

def detect_emotion(imgpath):
    print(imgpath)
    image = cv2.imread(imgpath)

    analyze = DeepFace.analyze(image, actions=['emotion'])  
    pprint(analyze)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--img_path', metavar='I', type=str, help='Image file with face to detect emotion.')
    args = parser.parse_args()

    detect_emotion(args.img_path)
