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

def add_salt_and_pepper_noise(image, snr):
    noisy_image = image.copy()
    num_salt = np.ceil((1 - snr) * image.size * 0.5)
    num_pepper = np.ceil((1 - snr) * image.size * 0.5)

    # Add salt noise
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1], :] = 255

    # Add pepper noise
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[coords[0], coords[1], :] = 0

    return noisy_image

if __name__ == '__main__':
    ############################
    ### TODO: YOUR CODE HERE ###

    # Step 1: Read image “FlowerA.jpg” from the data folder with option cv2.IMREAD_COLOR
    original_image = cv2.imread('data/FlowerA.jpg', cv2.IMREAD_COLOR)

    # Step 2: View the image on screen using cv2.imshow
    cv2.imshow('Original Image', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 3: Add salt-and-pepper noise to the color image using a signal-to-noise ratio equal to 0.9
    noisy_image = add_salt_and_pepper_noise(original_image, snr=0.9)

    # Step 4: Save the noisy image inside the output folder
    cv2.imwrite('output/31_q1_noisy_9_FlowerA.jpg', noisy_image)
    cv2.imshow('Noisy Image', noisy_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 5: Apply the Mean Filter
    mean_filtered_image = cv2.blur(noisy_image, (3, 3), borderType=cv2.BORDER_REPLICATE)

    # Step 6: Save the image inside the output folder
    cv2.imwrite('output/31_q1_Mean_noisy_9_FlowerA.jpg', mean_filtered_image)
    cv2.imshow('Mean Filtered Image', mean_filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 7: Apply Gaussian filter
    gaussian_filtered_image = cv2.GaussianBlur(noisy_image, (3, 3), 0, borderType=cv2.BORDER_REPLICATE)

    # Step 8: Save the image inside the output folder
    cv2.imwrite('output/31_q1_Gauss_noisy_9_FlowerA.jpg', gaussian_filtered_image)
    cv2.imshow('Gaussian Filtered Image', gaussian_filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 9: Apply Median filter
    median_filtered_image = cv2.medianBlur(noisy_image, 3)

    # Step 10: Save the image inside the output folder
    cv2.imwrite('output/31_q1_median_noisy_9_FlowerA.jpg', median_filtered_image)
    cv2.imshow('Median Filtered Image', median_filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 13: Repeat with SNR=0.8 and save images
    noisy_image_8 = add_salt_and_pepper_noise(original_image, snr=0.8)
    cv2.imwrite('output/31_q1_noisy_8_FlowerA.jpg', noisy_image_8)

    mean_filtered_image_8 = cv2.blur(noisy_image_8, (3, 3), borderType=cv2.BORDER_REPLICATE)
    cv2.imwrite('output/31_q1_Mean_noisy_8_FlowerA.jpg', mean_filtered_image_8)

    gaussian_filtered_image_8 = cv2.GaussianBlur(noisy_image_8, (3, 3), 0, borderType=cv2.BORDER_REPLICATE)
    cv2.imwrite('output/31_q1_Gauss_noisy_8_FlowerA.jpg', gaussian_filtered_image_8)

    median_filtered_image_8 = cv2.medianBlur(noisy_image_8, 3)
    cv2.imwrite('output/31_q1_median_noisy_8_FlowerA.jpg', median_filtered_image_8)
    #
    ### END OF STUDENT CODE ####
    ############################
