"""
Group Number: 31
Group Names :
     Pillay, Steven
     Hodovaniuk, Olha
     Sun, Ruyuan
     Iqbal, Syed
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    ############################
    ### TODO: YOUR CODE HERE ###
    # Step 1: Read image "seacolor.jpg" from the data folder with option cv2.IMREAD_COLOR
    color_image = cv2.imread('data/seacolor.jpg', cv2.IMREAD_COLOR)

    # Step 2: View the image on screen using cv2.imshow
    cv2.imshow('Original Color Image', color_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 3: Convert the input image to HSV color mode, and then split the image channels
    hsv_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
    h_channel, s_channel, v_channel = cv2.split(hsv_image)

    # Step 4: Apply histogram equalization to the V channel only
    equalized_v_channel = cv2.equalizeHist(v_channel)

    # Step 5: Use the newly equalized V channel to merge the image channels again
    equalized_hsv_image = cv2.merge((h_channel, s_channel, equalized_v_channel))
    equalized_color_image = cv2.cvtColor(equalized_hsv_image, cv2.COLOR_HSV2BGR)

    # Step 6: View the produced image from Step 5 on screen using cv2.imshow
    cv2.imshow('Equalized Color Image', equalized_color_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 7: Save the produced image from Step 5
    cv2.imwrite('output/31_q2_seacolor_eq.jpg', equalized_color_image)
    #
    ### END OF STUDENT CODE ####
    ############################