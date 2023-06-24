#=============================# 
#                             #
#     image 'de-keystoner'    #
#       HaydenJ 24/6/23       #
#                             #
#     ------         -------  #
#    /     /         |     |  #
#   /     /    -->   |     |  #
#  /_____/           |_____|  #
#                             #
#=============================# 

# Libs
import cv2
import numpy as np
####

# Vars
points = []
currentPoint = []
lastPoint = []
####

# Image loading
fileName = 'test.jpg'
img = cv2.imread(fileName)
imgMaster = img.copy()
imgTemp = img.copy()
####

# Mouse event function
def mouseCallback(event, x, y, flags, param):

    global lastPoint, currentPoint, imgTemp

    if event == cv2.EVENT_LBUTTONDOWN:

        if len(points) < 4:

            points.append([x, y])
            lastPoint = ([x, y])

            cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
            imgTemp = img.copy()

    elif event == cv2.EVENT_MOUSEMOVE and len(points) < 4:

        currentPoint = ([x, y])
####


# Create a window and bind Mouse function
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouseCallback)

# Drawing loop and current segment code inspired by:
# https://github.com/sampan-s-nayak/manual_polygon_drawer/blob/master/polygon_drawer.py
while True:

    if len(points) >= 1 and len(points) <= 2:

        if(currentPoint != lastPoint):
            img = imgTemp.copy()

        cv2.line(img, (lastPoint[0], lastPoint[1]), (currentPoint[0], currentPoint[1]), (255, 0, 0))

    elif len(points) >= 2 and len(points) <= 3:

        if(currentPoint != lastPoint):
            img = imgTemp.copy()

        cv2.line(img, (lastPoint[0], lastPoint[1]),(currentPoint[0], currentPoint[1]), (255, 0, 0))
        cv2.line(img, (points[0][0], points[0][1]),(currentPoint[0], currentPoint[1]), (255, 0, 0))

    cv2.imshow('Image', img)

    key = cv2.waitKey(1) & 0xFF

    # Exit loop if esc
    if key == 27:
        break

    # Keystone transformation
    if len(points) == 4:
        width, height = img.shape[1], img.shape[0]
        
        trueWidth  = np.sqrt( np.abs(points[0][0] - points[1][0]) ** 2 + np.abs(points[0][1] - points[1][1]) ** 2).astype(int)
        trueHeight = np.sqrt( np.abs(points[0][0] - points[3][0]) ** 2 + np.abs(points[0][1] - points[3][1]) ** 2).astype(int)
        
        srcPoints = np.float32(points)
        dstPoints = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
        
        matrix = cv2.getPerspectiveTransform(srcPoints, dstPoints)
        
        keystoneImg = cv2.warpPerspective(imgMaster, matrix, (width, height))
        #keystoneImg = cv2.warpPerspective(imgMaster, matrix, (trueWidth, trueHeight))
        adjImg = cv2.resize(keystoneImg, (trueWidth, trueHeight))

        #cv2.imshow('Keystone Image', keystoneImg)
        cv2.imshow('Keystone Image', adjImg)
        
        cv2.imwrite(('fixed_' + fileName),adjImg)
####

cv2.destroyAllWindows()
