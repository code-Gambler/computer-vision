"""
Group Number: 31
Group Names :
     Olha Hodovaniuk
     Ruyuan Sun
     Steven David Pillay
     Syed Moonis Iqbal
"""

"""
Question 1: Getting familiar with image manipulation in python - opencv
Read the image "bicycle.bmp" from the <data> directory
using opencv flag cv2.IMREAD_UNCHANGED
and then find and print the following information about this image

a)	find image height (number of rows)
b)	find image width (number of columns)
c)	find image number of channels
d)	find image datatype
e)	find image number of pixels
f)	convert the image to gray level and then save it in output directory as "bicyclegray.jpg"
g)	find the maximum value of the pixel values
h)	Calculate the mean/average of the pixel values
i)	Change the pixel values of the image in the following way:
    all pixels’ values less than the average value calculated at (h) will be equal to 0
    and all the other pixels will be equal to 1. Then, save it in output directory as "bicycleoutA.jpg"
j)	What type of image that is  generated at (i)?


no need to do this
Repeat the about information using the following opencv flag
cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE

"""
import cv2
import numpy as np

if __name__ == '__main__':

    ############################
    ### TODO: YOUR CODE HERE ###

    # Read the image "bicycle.bmp" from the <data> directory
    img = cv2.imread('data/bicycle.bmp', cv2.IMREAD_UNCHANGED)

    # find image height (number of rows)
    height = img.shape[0]

    # find image width (number of columns)
    width = img.shape[1]

    # find image number of channels
    channels = img.shape[2]

    # find image datatype
    datatype = img.dtype

    # find image number of pixels
    pixels = img.size

    # convert the image to gray level and then save it in output directory as "bicyclegray.jpg"
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('output/bicyclegray.jpg', gray)

    # find the maximum value of the pixel values
    max_value = np.max(gray)

    # Calculate the mean/average of the pixel values
    mean = np.mean(gray)

    # Change the pixel values of the image in the following way:
    # all pixels’ values less than the average value calculated at (h) will be equal to 0
    # and all the other pixels will be equal to 1. Then, save it in output directory as "bicycleoutA.jpg"
    outA = np.where(gray < mean, 0, 1) * 255

    cv2.imwrite('output/bicycleoutA.jpg', outA)

    # What type of image that is generated at (i)?
    # The image produced is a binary image or an image with only 2 levels of intensity
    print(f'Height: {height}')
    print(f'Width: {width}')
    print(f'Channels: {channels}')
    print(f'Datatype: {datatype}')
    print(f'Pixels: {pixels}')
    print(f'Max value: {max_value}')
    print(f'Mean: {mean}')
    print(f'The image produced is a binary image or an image with only 2 levels of intensity')

    ### END OF STUDENT CODE ####
    ############################

