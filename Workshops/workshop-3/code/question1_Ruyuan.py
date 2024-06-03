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
import math

if __name__ == '__main__':
    # Ensure the output directory exists
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # a) Create color image (full black image) with the size 480 x 640, and then display this image
    # (640, 480, 3) Height, Width, Number of Channels
    black_image = np.zeros((640, 480, 3), dtype=np.uint8)
    cv2.imshow('Black Image', black_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # b) Save the black image in the output file with the name “black.jpg”
    cv2.imwrite(os.path.join(output_dir, 'black.jpg'), black_image)

    # c) Draw two red lines on the black image with thickness 4
    # One line divides the width into two halves
    cv2.line(black_image, (240, 0), (240, 640), (0, 0, 255), 4)
    # One line divides the height into two halves
    cv2.line(black_image, (0, 320), (480, 320), (0, 0, 255), 4)
    # d) Display the result image
    cv2.imshow('Two Lines', black_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Save the result image
    cv2.imwrite(os.path.join(output_dir, 'twolines.jpg'), black_image)

    # e) Randomly pick one of the empty four quarters and draw a white rectangle
    quarters = [
        ((0, 0), (240, 320)),
        ((240, 0), (480, 320)),
        ((0, 320), (240, 640)),
        ((240, 320), (480, 640))
    ]
    # Randomly select an integer from 0 to 3. This integer selected_quarter is an index into the quarters list.
    selected_quarter = np.random.choice(len(quarters))
    # quarters[selected_quarter] gets the element at index selected_quarter in the quarters list, which is a tuple
    # containing two coordinates (the upper left corner and the lower right corner).
    top_left = quarters[selected_quarter][0]
    bottom_right = quarters[selected_quarter][1]

    rect_x = np.random.randint(top_left[0], bottom_right[0] - 75)
    rect_y = np.random.randint(top_left[1], bottom_right[1] - 50)
    cv2.rectangle(black_image, (rect_x, rect_y), (rect_x + 75, rect_y + 50), (255, 255, 255), -1)

    # Display the result image
    cv2.imshow('White Rectangle', black_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Save the result image
    cv2.imwrite(os.path.join(output_dir, 'rectangle.jpg'), black_image)

    # f) Pick one of the remaining empty quarters randomly, and draw a blue circle with a radius of 40
    # range(4) generates a sequence of integers from 0 to 3, [0, 1, 2, 3].
    remaining_quarters = list(range(4))
    remaining_quarters.remove(selected_quarter)
    selected_quarter = np.random.choice(remaining_quarters)
    top_left = quarters[selected_quarter][0]
    bottom_right = quarters[selected_quarter][1]

    circle_x = np.random.randint(top_left[0] + 40, bottom_right[0] - 40)
    circle_y = np.random.randint(top_left[1] + 40, bottom_right[1] - 40)
    cv2.circle(black_image, (circle_x, circle_y), 40, (255, 0, 0), -1)

    # Display the result image
    cv2.imshow('Blue Circle', black_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Save the result image
    cv2.imwrite(os.path.join(output_dir, 'circle.jpg'), black_image)

    # g) Pick one of the remaining empty quarters randomly, and draw a yellow pentagon
    remaining_quarters.remove(selected_quarter)
    selected_quarter = np.random.choice(remaining_quarters)
    top_left = quarters[selected_quarter][0]
    bottom_right = quarters[selected_quarter][1]

    # The size of the pentagon should be greater than 20 and less than half of the short side of the selected quarter
    size = np.random.randint(21, 120)

    # Make sure the distance from the center of the pentagon to the border of the selected area is greater than the size
    # of the pentagon
    center_x = np.random.randint(top_left[0] + size, bottom_right[0] - size)
    center_y = np.random.randint(top_left[1] + size, bottom_right[1] - size)

    # Define the pentagon points
    angles = [i * (2 * math.pi / 5) for i in range(5)]  # 5 vertices
    pentagon_points = np.array([[
        (int(center_x + size * math.cos(angle)), int(center_y + size * math.sin(angle)))
        for angle in angles
    ]], np.int32)

    cv2.fillPoly(black_image, pentagon_points, (0, 255, 255))

    # Display the result image
    cv2.imshow('Yellow Pentagon', black_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Save the result image
    cv2.imwrite(os.path.join(output_dir, 'pentagon.jpg'), black_image)

    # h) Pick the last remaining quarter and then write your group name in green color
    remaining_quarters.remove(selected_quarter)
    selected_quarter = remaining_quarters[0]
    top_left = quarters[selected_quarter][0]
    bottom_right = quarters[selected_quarter][1]

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Group thirty-one'

    # Adjust font scale to fit text in the quarter
    font_scale = 1
    font_thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]

    while text_size[0] > (bottom_right[0] - top_left[0]) or text_size[1] > (bottom_right[1] - top_left[1]):
        font_scale -= 0.1
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = top_left[0] + (bottom_right[0] - top_left[0] - text_size[0]) // 2
    text_y = top_left[1] + (bottom_right[1] - top_left[1] + text_size[1]) // 2
    cv2.putText(black_image, text, (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness, cv2.LINE_AA)

    # Display the result image
    cv2.imshow('Group Name', black_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Save the image into the output directory named “ws3q1.jpg”
    cv2.imwrite(os.path.join(output_dir, 'ws3q1.jpg'), black_image)

    # raise NotImplementedError('Implementation for `Question ` in `workshop` is missing')
    #
    ### END OF STUDENT CODE ####
    ############################
