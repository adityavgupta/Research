from PIL import Image
from imutils import paths
import numpy as np
import cv2
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", type=str, default="SVD_study", help="path to load the directory containing the images to be split")
args = vars(ap.parse_args())

imagePaths = paths.list_images(args["dataset"])

k=469
for imagePath in imagePaths:
	image = Image.open(imagePath)
	data = image.getdata() 

	# Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
	r = [(d[0], 0, 0) for d in data]
	g = [(0, d[1], 0) for d in data]
	b = [(0, 0, d[2]) for d in data]

	#image.putdata(r)
	#image.save('r%s.png' % k)
	
	image.putdata(g)
	image.save('g%s.png' % k)

	#image.putdata(b)
	#image.save('b%s.png' % k)
	print('g%s.png' % k)
	k += 1


