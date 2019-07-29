from PIL import Image
from imutils import paths
import numpy as np
import cv2
import os
import argparse

#construct argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", type=str, default="SVD_study", help="path to load the directory containing the images to be split")
args = vars(ap.parse_args())

#make a list of directories
imagePaths = paths.list_images(args["dataset"])

#set counter to name output files
k=1

#for each image inside each directory split the image into its rgb channel
for imagePath in imagePaths:
	image = Image.open(imagePath)
	data = image.getdata() 

	# Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
	r = [(d[0], 0, 0) for d in data]
	g = [(0, d[1], 0) for d in data]
	b = [(0, 0, d[2]) for d in data]

    #save each image with status on the number of image reached
	image.putdata(r)
	image.save('r%s.png' % k)
	print('r%s.png' % k)
    
	image.putdata(g)
	image.save('g%s.png' % k)
    print('g%s.png' % k)
        
	image.putdata(b)
	image.save('b%s.png' % k)
	print('b%s.png' % k)
    
    #update name counter
	k += 1


