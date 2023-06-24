# keystone_correction
a simple python script for keystone correction in images
## Usage :
1) starting from the top left-hand and going clockwise, click the four corners of the ROI
2) the image will be automatically cropped, corrected, and saved as fixed_image.jpg

Original image with ROI

![Original image with ROI](https://github.com/HaydenRJones/keystone_correction/blob/main/assets/example1.png?raw=true)

Output image after correction

![Output image after correction](https://github.com/HaydenRJones/keystone_correction/blob/main/assets/example2.png?raw=true)

## Requirements :
- python 3.xx
- numpy
- cv2

## Todo :
- better file handiling
  - deal with batches of files (ideally everything in a target folder)
  - multiple ROIs from a single image
-  zoom function for better cusor placement
-  more flexible ROI selection (starting from any corner)
-  general optimisation / decluttering
