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
import os

if __name__ == '__main__':
    ############################
    ### TODO: YOUR CODE HERE ###

    # Ensure the output directory exists
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Step 1: Read the image "Flower.bmp" from the data folder with option cv2.IMREAD_COLOR
    original_image = cv2.imread('data/Flower.bmp', cv2.IMREAD_COLOR)

    # Step 2: View the image on screen using cv2.imshow
    cv2.imshow('Original Image', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 3: Convert the image from the BGR color model to the HSV model
    hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV Image', hsv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_FlowerHSV.jpg'), hsv_image)

    # Step 4: Split the image into different channels (Hue, Saturation, and Value)
    h_channel, s_channel, v_channel = cv2.split(hsv_image)

    cv2.imshow('Hue Channel', h_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_FlowerHCh.jpg'), h_channel)

    cv2.imshow('Saturation Channel', s_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_FlowerSCh.jpg'), s_channel)

    cv2.imshow('Value Channel', v_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_FlowerVCh.jpg'), v_channel)

    # Step 6: Create a new image with the same shape as the original image using numpy.zeros
    new_image = np.zeros_like(hsv_image)

    # Step 7: Add the Hue channel to the new image and view the result
    new_image[:, :, 0] = h_channel
    cv2.imshow('Hue Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_himage.jpg'), new_image)

    # Step 8: Add the Saturation channel to the resulting image from step 7 and view the result
    new_image[:, :, 1] = s_channel
    cv2.imshow('Hue Saturation Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_hsimage.jpg'), new_image)

    # Step 9: Add the Value channel to the resulting image from step 8 and view the result
    new_image[:, :, 2] = v_channel
    cv2.imshow('HSV Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_hsvimage.jpg'), new_image)

    # Step 11: Repeat the same process for "falltreenature.jpg"
    original_image = cv2.imread('data/falltreenature.jpg', cv2.IMREAD_COLOR)
    cv2.imshow('Original Image', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV Image', hsv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_tree_HSV.jpg'), hsv_image)

    h_channel, s_channel, v_channel = cv2.split(hsv_image)

    cv2.imshow('Hue Channel', h_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_tree_HCh.jpg'), h_channel)

    cv2.imshow('Saturation Channel', s_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_tree_SCh.jpg'), s_channel)

    cv2.imshow('Value Channel', v_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_tree_VCh.jpg'), v_channel)

    new_image = np.zeros_like(hsv_image)

    new_image[:, :, 0] = h_channel
    cv2.imshow('Hue Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_tree_himage.jpg'), new_image)

    new_image[:, :, 1] = s_channel
    cv2.imshow('Hue Saturation Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_tree_hsimage.jpg'), new_image)

    new_image[:, :, 2] = v_channel
    cv2.imshow('HSV Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q2_tree_hsvimage.jpg'), new_image)

    ### END OF STUDENT CODE ####
    ############################
