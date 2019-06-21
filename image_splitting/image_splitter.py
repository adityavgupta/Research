# Aditya Vikram Gupta
# Custom file for splitting sample histology images into 512x512
# June 20, 2019

from PIL import Image
from imutils import paths
import numpy as np
import argparse
import os

# construct argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", type=str, default="image_data", help="path to load the directory containing the images to be split")
args = vars(ap.parse_args())

#grab the image path in the input dataset directory
print("[INFO] loading images...")
imagePaths = paths.list_images(args["dataset"])
chopsize = 512
# loop over our input images
for imagePath in imagePaths:
	# load the input image frim the disk, split the images
# and update our list of split images
	image=Image.open(imagePath)
	width, height = image.size
	k=1
	#save chops of the original images
	for x0 in range (0, width, chopsize):
		for y0 in range (0, height, chopsize):
			box = (x0, y0, 
				x0+chopsize if x0+chopsize < width else width - 1,
				y0+chopsize if y0+chopsize < height else height - 1)
			b = Image.new("RGB", (512, 512), "#ddd")
			b = image.crop(box)
			o = b.save("IMG_%s.png" % k)
		
			k +=1
