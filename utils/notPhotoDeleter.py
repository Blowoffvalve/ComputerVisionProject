from fastai.vision import *
import os

path = Path("../Data/")
photoExtension = [".jpg", ".JPG", ".png", ".jpeg", ".PNG"]
for dir in os.listdir(path):
	if os.path.isdir(path/dir):
		for file in os.listdir(path/dir):
			filename, fileExtension = os.path.splitext(file)
			if not fileExtension in photoExtension:
				print("Removing " + dir+"/"+ file)
				os.remove(path/dir/file)
				