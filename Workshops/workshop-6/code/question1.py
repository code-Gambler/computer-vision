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
    # Step 1: Read the image "seagrayscale.jpg" from the data folder with option cv2.IMREAD_GRAYSCALE
    original_image = cv2.imread('data/seagrayscale.jpg', cv2.IMREAD_GRAYSCALE)

    # Step 2: View the image on screen using cv2.imshow
    cv2.imshow('Original Image', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 3: Compute histogram of the input image "seagrayscale.jpg"
    histogram, bins = np.histogram(original_image.flatten(), 256, [0, 256])

    # Step 4: Ensure matplotlib library is imported
    import matplotlib.pyplot as plt

    # Step 5: Create a figure instance
    plt.figure()

    # Step 6: Plot the computed histogram
    plt.plot(histogram)
    plt.title('Histogram for Original Image')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.grid(True)

    # Step 7: Save the histogram plot
    plt.savefig('output/31_q1_seagrayscale_hist.jpg')

    # Step 8: Display the histogram plot
    plt.show()

    # Step 9: Compute the Cumulative Distribution Function (CDF)
    cdf = histogram.cumsum()

    # Step 10: Create a figure instance for the CDF plot
    plt.figure()

    # Step 11: Plot the computed CDF
    plt.plot(cdf, color='b')
    plt.title('CDF for Original Image')
    plt.xlabel('Pixel Value')
    plt.ylabel('Cumulative Frequency')
    plt.grid(True)

    # Step 12: Save the CDF plot
    plt.savefig('output/31_q1_seagrayscale_CDF.jpg')

    # Step 13: Apply histogram equalization to the image "seagrayscale.jpg"
    equalized_image = cv2.equalizeHist(original_image)
    cv2.imwrite('output/31_q1_seagrayscale_eq.jpg', equalized_image)

    # Step 14: View the produced image from Step 13
    cv2.imshow('Equalized Image', equalized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 15: Compute the histogram for the image produced by Step 13
    eq_histogram, eq_bins = np.histogram(equalized_image.flatten(), 256, [0, 256])

    # Step 16: Create a figure instance for the equalized histogram
    plt.figure()

    # Step 17: Plot the computed histogram for the equalized image
    plt.plot(eq_histogram)
    plt.title('Histogram for Equalized Image')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.grid(True)

    # Step 18: Save the histogram plot for the equalized image
    plt.savefig('output/31_q1_seagrayscale_eq_hist.jpg')

    # Step 19: Compute the Cumulative Distribution Function (CDF) of the equalized histogram
    eq_cdf = eq_histogram.cumsum()

    # Step 20: Create a figure instance for the equalized CDF plot
    plt.figure()

    # Step 21: Plot the computed CDF for the equalized image
    plt.plot(eq_cdf, color='b')
    plt.title('CDF for Equalized Image')
    plt.xlabel('Pixel Value')
    plt.ylabel('Cumulative Frequency')
    plt.grid(True)

    # Step 22: Save the CDF plot for the equalized image
    plt.savefig('output/31_q1_seagrayscale_eq_CDF.jpg')
    #
    ### END OF STUDENT CODE ####
    ############################