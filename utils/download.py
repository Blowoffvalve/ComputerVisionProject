from fastai.vision import *
import os
from PIL import Image


extension = ".csv"
breeds = []
path = Path("../Data/")
breeds += [each for each in os.listdir(path) if each.endswith(extension)]
imagesPerBreed = 250

#Download files
for breed in breeds:
	print("Retrieving images for {} breed".format(breed.split(extension)[0]))
	dest = path/breed.split(extension)[0]
	dest.mkdir(parents=True, exist_ok=True)
	download_images(path/breed, dest, max_pics = imagesPerBreed, max_workers=0)

#Delete unnecessary or invalid files
photoExtension = [".jpg", ".JPG", ".png", ".jpeg", ".PNG"]
for dir in os.listdir(path):
	if os.path.isdir(path/dir):
		for file in os.listdir(path/dir):
			filename, fileExtension = os.path.splitext(file)
			#Remove files with extensions that aren't jpg or png
			if not fileExtension in photoExtension:
				print("Removing " + dir+"/"+ file)
				os.remove(path/dir/file)
			else:
				#Remove images that can't be opened by PIL as they're most likely corrupt
				try:
					Image.open(path/dir/file)
				except IOError:
					os.remove(path/dir/file)
					print("Removing " + dir+"/"+ file + " Because it is invalid")
				