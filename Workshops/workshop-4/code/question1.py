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

    # Step 1: Read the image "Flower.bmp" from the data folder with option cv2.IMREAD_COLOR
    image_path = 'data/Flower.bmp'
    output_dir = 'output'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read and display the original image
    original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    cv2.imshow('Original Image', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 3: Split image channels and view them separately, then save each channel as an image inside the output folder
    blue_channel, green_channel, red_channel = cv2.split(original_image)

    cv2.imshow('Blue Channel', blue_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q1_FlowerBlueCh.jpg'), blue_channel)

    cv2.imshow('Green Channel', green_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q1_FlowerGreenCh.jpg'), green_channel)

    cv2.imshow('Red Channel', red_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q1_FlowerRedCh.jpg'), red_channel)

    # Step 5: Create a new image with the same shape as the original image using numpy.zeros
    new_image = np.zeros_like(original_image)

    # `:` is the slicing operator. All elements in the corresponding dimension should be selected
    # height, width, channels
    # Step 6: Add the blue channel to the new image and view the result
    new_image[:, :, 0] = blue_channel
    cv2.imshow('Blue Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q1_bimage.jpg'), new_image)

    # Step 7: Add the green channel to the resulting image from step 6 and view the result
    new_image[:, :, 1] = green_channel
    cv2.imshow('Blue Green Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q1_bgimage.jpg'), new_image)

    # Step 8: Add the red channel to the resulting image from step 7 and view the result
    new_image[:, :, 2] = red_channel
    cv2.imshow('BGR Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q1_bgrimage.jpg'), new_image)

    # Step 10: Repeat the same process for "falltreenature.jpg"
    image_path = 'data/falltreenature.jpg'

    # Read and display the new image
    original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    cv2.imshow('Original Image', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Split image channels and view them separately, then save each channel as an image inside the output folder
    blue_channel, green_channel, red_channel = cv2.split(original_image)

    cv2.imshow('Blue Channel', blue_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q1_treeBlueCh.jpg'), blue_channel)

    cv2.imshow('Green Channel', green_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q1_treeGreenCh.jpg'), green_channel)

    cv2.imshow('Red Channel', red_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q1_treeRedCh.jpg'), red_channel)

    # Create a new image with the same shape as the original image using numpy.zeros
    new_image = np.zeros_like(original_image)

    # Add the blue channel to the new image and view the result
    new_image[:, :, 0] = blue_channel
    cv2.imshow('Blue Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q1_tree_bimage.jpg'), new_image)

    # Add the green channel to the resulting image from step 6 and view the result
    new_image[:, :, 1] = green_channel
    cv2.imshow('Blue Green Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q1_tree_bgimage.jpg'), new_image)

    # Add the red channel to the resulting image from step 7 and view the result
    new_image[:, :, 2] = red_channel
    cv2.imshow('BGR Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(output_dir, '31_q1_tree_bgrimage.jpg'), new_image)

    ### END OF STUDENT CODE ####
    ############################
