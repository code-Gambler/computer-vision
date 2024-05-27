"""
Group Number: 31
Group Names :
     Olha Hodovaniuk
     Ruyuan Sun
     Steven David Pillay
     Syed Moonis Iqbal
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

if __name__ == '__main__':
    levels = [256, 128, 64, 32, 16, 8, 4, 2]
    image = cv2.imread('data/lena.tif', cv2.IMREAD_GRAYSCALE)

    for level in levels:
        image_level = (image // (256 // level)) * 256 // level
        cv2.imwrite(f'output/lena{level}.jpg', image_level)

