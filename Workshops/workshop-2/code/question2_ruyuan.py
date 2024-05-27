"""
Group Number: 31
Group Names :
     Pillay, Steven
     Hodovaniuk, Olha
     Sun, Ruyuan
     Iqbal, Syed
"""


"""
Question 2:
Reducing the Number of Intensity Levels in an Image
Write a computer program capable of reducing the number of intensity levels in a gray image from 256 levels to 2 levels,
in integer powers of 2. That is intensity levels: 256 default, 128, 64, 32, 16, 8, 4, 2.
Use image "lena.tif" from data directory
Note: Your code should generate the image with the required intensity and then write/save the image
to the output directory.
The name of generated images as following lena256.jpg, lena128.jpg, lena64.jpg, lena32.jpg, lena16.png,
 lena8.png, lena4.png, and lena2.png.




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
    img = cv2.imread('data/lena.tif', cv2.IMREAD_GRAYSCALE)


    # Function to reduce intensity levels
    def reduce_intensity_levels(image, levels):
        factor = 256 // levels
        reduced_img = (image // factor) * factor
        return reduced_img


    # Intensity levels
    levels_list = [256, 128, 64, 32, 16, 8, 4, 2]
    filenames = ['lena256.jpg', 'lena128.jpg', 'lena64.jpg', 'lena32.jpg', 'lena16.png', 'lena8.png', 'lena4.png',
                 'lena2.png']

    # Loops through each pair of levels and filename.
    for levels, filename in zip(levels_list, filenames):
        reduced_img = reduce_intensity_levels(img, levels)
        cv2.imwrite(os.path.join(output_dir, filename), reduced_img)

    # raise NotImplementedError('Implementation for `Question ` in `workshop2` is missing')

    ### END OF STUDENT CODE ####
    ############################

