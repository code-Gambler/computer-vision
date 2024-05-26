
"""
Group Number: 31
Group Names :
     Pillay, Steven
     Hodovaniuk, Olha
     Sun, Ruyuan
     Iqbal, Syed
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
import os


if __name__ == '__main__':


    ############################
    ### TODO: YOUR CODE HERE ###

    # Ensure the output directory exists
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the image
    img = cv2.imread('data/bicycle.bmp', cv2.IMREAD_COLOR)

    # a) Image height
    height = img.shape[0]
    print(f"Image height: {height}")

    # b) Image width
    width = img.shape[1]
    print(f"Image width: {width}")

    # c) Number of channels
    channels = img.shape[2] if len(img.shape) > 2 else 1
    print(f"Number of channels: {channels}")

    # d) Image datatype
    datatype = img.dtype
    print(f"Image datatype: {datatype}")

    # e) Number of pixels
    num_pixels = img.size
    print(f"Number of pixels: {num_pixels}")

    # f) Convert to gray level and save
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(output_dir, 'bicyclegray.jpg'), gray_img)

    # g) Maximum pixel value
    max_val = np.max(gray_img)
    print(f"Maximum pixel value: {max_val}")

    # h) Mean pixel value
    mean_val = np.mean(gray_img)
    print(f"Mean pixel value: {mean_val}")

    # i) Change pixel values and save
    binary_img = np.where(gray_img < mean_val, 0, 1).astype(np.uint8)
    cv2.imwrite(os.path.join(output_dir, 'bicycleoutA.jpg'), binary_img * 255)

    # j) Type of image generated
    print("The image generated is a binary image.")

    # raise NotImplementedError('Implementation for `Question ` in `workshop2` is missing')

    ### END OF STUDENT CODE ####
    ############################

