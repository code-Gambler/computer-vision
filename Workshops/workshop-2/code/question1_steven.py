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

def read_image(path):
    return cv2.imread(path, cv2.IMREAD_UNCHANGED)

def get_height(img):
    return img.shape[0]
def get_width(img):
    return img.shape[1]
def get_channels(img):
    return img.shape[2]
def get_datatype(img):
    return img.dtype

def get_pixels(img):
    return img.size

def convert_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def write_image(path, img):
    cv2.imwrite(path, img)

def get_max(img):
    return np.max(img)

def get_mean(img):
    return np.mean(img)


if __name__ == '__main__':
    bicycle_img = read_image('data/bicycle.bmp')
    print(f'Height: {get_height(bicycle_img)}')
    print(f'Width: {get_width(bicycle_img)}')
    print(f'Channels: {get_channels(bicycle_img)}')
    print(f'Datatype: {get_datatype(bicycle_img)}')
    print(f'Pixels: {get_pixels(bicycle_img)}')
    gray_bicycle = convert_grayscale(bicycle_img)
    print(f'Max value: {get_max(gray_bicycle)}')
    print(f'Mean: {get_mean(gray_bicycle)}')
    # Change the pixel values of the image in the following way:
    # all pixels’ values less than the average value calculated at (h) will be equal to 0
    # and all the other pixels will be equal to 1. Then, save it in output directory as "bicycleoutA.jpg"
    outA = np.where(gray_bicycle < get_mean(gray_bicycle), 0, 1) * 255
    write_image('output/bicycleoutA.jpg', outA)
    write_image('output/bicyclegray.jpg', gray_bicycle)
    print(f'The image produced is a binary image or an image with only 2 levels of intensity')

