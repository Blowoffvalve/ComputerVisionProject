from fastai.vision import Path
import os
from PIL import Image

path = Path("../Data/")

#Delete unnecessary or invalid files
photoExtension = [".jpg", ".JPG", ".png", ".jpeg", ".PNG"]
for dir in os.listdir(path):
	if os.path.isdir(path/dir):
		for file in os.listdir(path/dir):
			#print("Examining " + dir+"/"+ file)
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
				