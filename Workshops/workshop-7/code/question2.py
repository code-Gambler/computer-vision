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

def compute_mse(image1, image2):
    return np.mean((image1 - image2) ** 2)

if __name__ == '__main__':
    ############################
    ### TODO: YOUR CODE HERE ###

    # Step 1: Read image “peppers.tif” from the data folder with option cv2.IMREAD_GRAYSCALE
    original_image = cv2.imread('data/peppers.tif', cv2.IMREAD_GRAYSCALE)

    # Step 2: View the image on screen using cv2.imshow
    cv2.imshow('Original Image', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 3: Read image “peppers_noisy.tif” from the data folder with option cv2.IMREAD_GRAYSCALE
    noisy_image = cv2.imread('data/peppers_noisy.tif', cv2.IMREAD_GRAYSCALE)

    # Step 4: View the image on screen using cv2.imshow
    cv2.imshow('Noisy Image', noisy_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 5: Compute the mean-squared error (MSE)
    mse_noisy = compute_mse(original_image, noisy_image)
    print(f"MSE between original and noisy images: {mse_noisy}")

    # Step 6-8: Apply mean filter with different sizes and compute MSE
    filter_sizes = [3, 5, 7, 9, 11]
    mse_values = []

    for size in filter_sizes:
        filtered_image = cv2.blur(noisy_image, (size, size), borderType=cv2.BORDER_REPLICATE)
        mse = compute_mse(original_image, filtered_image)
        mse_values.append((size, mse))
        cv2.imwrite(f'output/31_q2_peppers_filtered_{size}.jpg', filtered_image)

    # Step 8: Find a filter width that minimizes the mean-squared error
    best_size, best_mse = min(mse_values, key=lambda x: x[1])
    print(f"Best filter size: {best_size} with MSE: {best_mse}")

    # Plotting the MSE values for different filter sizes
    sizes, mses = zip(*mse_values)
    plt.plot(sizes, mses, marker='o')
    plt.title('MSE vs Filter Size')
    plt.xlabel('Filter Size')
    plt.ylabel('MSE')
    plt.grid(True)
    plt.savefig('output/31_q2_peppers_mse_plot.jpg')
    plt.show()

    # Step 9: Display the filtered image with the smallest mean-squared error
    best_filtered_image = cv2.blur(noisy_image, (best_size, best_size), borderType=cv2.BORDER_REPLICATE)
    cv2.imwrite('output/31_q2_noisy_free_peppers.jpg', best_filtered_image)
    cv2.imshow('Best Filtered Image', best_filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #
    ### END OF STUDENT CODE ####
    ############################
