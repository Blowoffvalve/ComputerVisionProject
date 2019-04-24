from fastai.vision import *
import os
extension = ".csv"
breeds = []
path = Path("../Data/")
breeds += [each for each in os.listdir(path) if each.endswith(extension)]
for breed in breeds:
	print("Retrieving images for {} breed".format(breed.split(extension)[0]))
	dest = path/breed.split(extension)[0]
	dest.mkdir(parents=True, exist_ok=True)
	download_images(path/breed, dest, max_pics = 1, max_workers=0)
	
photoExtension = [".jpg", ".JPG", ".png", ".jpeg", ".PNG"]
for dir in os.listdir(path):
	if os.path.isdir(path/dir):
		for file in os.listdir(path/dir):
			filename, fileExtension = os.path.splitext(file)
			if not fileExtension in photoExtension:
				print("Removing " + dir+"/"+ file)
				os.remove(path/dir/file)
				