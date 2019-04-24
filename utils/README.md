### Utils
[download.py](https://github.com/Blowoffvalve/ComputerVisionProject/blob/master/utils/download.py) operates on a all .csv files in [/Data](https://github.com/Blowoffvalve/ComputerVisionProject/tree/master/Data). As each file contains URLs for an images with the file name denoting what class the images belong to. The following operations are carried out for each file:
1. A folder is created for each class and all the images for that class are downloaded to that folder. 
2. The images are checked to ensure their extension is either `.png`, `.jpg` or `.jpeg`. Files with other extensions are deleted
3. PIL.Image attempts to open the image. If it can't, the image is deleted as being corrupt