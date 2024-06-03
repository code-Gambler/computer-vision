"""
Group Number: 31
Group Names :
     Last name , First name
     .......
     .......


"""

import cv2
import numpy as np

if __name__ == '__main__':

    ############################
    ### TODO: YOUR CODE HERE ###
    
	# Create black image, size 480x640 with 3 channels
    img = np.zeros((640,480,3), np.uint8)
    
	# Save the image
    cv2.imwrite('output/black.jpg', img)

	# Draw two red lines with thckness 4
    cv2.line(img, (240,0), (240,640), (0,0,255), 4)
    cv2.line(img, (0,320), (480,320), (0,0,255), 4)

    # Display the image
    cv2.imshow('image', img)
    cv2.waitKey(1000)
    
	# Save the image
    cv2.imwrite('output/twolines.jpg', img)
    
	# Randomly pick one quadrant
    quadrants = [(0, 0, 240, 320), (240, 0, 480, 320), (0, 320, 240, 640), (240, 320, 480, 640)]
    random_quadrant = quadrants[np.random.randint(0,4)]
    q1 = random_quadrant
    x1, y1, x2, y2 = random_quadrant
    max_x = x2 - 75
    max_y = y2 - 50
	
	# Randomly select a point in the quadrant so that the rectangle fits
    rectangle_x = np.random.randint(x1, max_x)
    rectangle_y = np.random.randint(y1, max_y)
    
	# Draw the rectangle
    cv2.rectangle(img, (rectangle_x, rectangle_y), (rectangle_x + 75, rectangle_y + 50), (255, 255, 255), -1)

	# Save the image
    cv2.imwrite('output/rectangle.jpg', img)
    
	# Draw a blue circle in one of the remaining quadrants
    while random_quadrant == q1:
        random_quadrant = quadrants[np.random.randint(0,4)]
    
    q2 = random_quadrant
    x1, y1, x2, y2 = random_quadrant
    min_x = x1 + 40
    min_y = y1 + 40
    max_x = x2 - 40
    max_y = y2 - 40
    
	# Randomly select a point in the quadrant so that the circle fits
    circle_x = np.random.randint(min_x, max_x)
    circle_y = np.random.randint(min_y, max_y)

	# Draw the circle
    cv2.circle(img, (circle_x, circle_y), 40, (255, 0, 0), -1)

	# Save the image
    cv2.imwrite('output/circle.jpg', img) 
    
	# Draw a yellow pentagon in one of the remaining quadrants
    while random_quadrant == q1 or random_quadrant == q2:
        random_quadrant = quadrants[np.random.randint(0,4)]

    q3 = random_quadrant
    x1, y1, x2, y2 = random_quadrant

    # Randomly generate the first vertex within the quadrant bounds, ensuring space for other vertices
    first_vertex_x = np.random.randint(x1, x2 - 100)
    first_vertex_y = np.random.randint(y1 + 20, y2 - 50)

    # Define the hardcoded offsets for the other vertices to form a pentagon
    offsets = [
    (0, 0),           # First vertex
    (50, -30),        # Second vertex
    (100, 0),         # Third vertex
    (80, 50),         # Fourth vertex
    (20, 50)          # Fifth vertex
]

    # Calculate the vertices based on the first random vertex and the offsets
    vertices = [(first_vertex_x + ox, first_vertex_y + oy) for ox, oy in offsets]
    pentagon_vertices = np.array(vertices, np.int32)

    # Draw the pentagon
    cv2.fillPoly(img, [pentagon_vertices], (0, 255, 255))
    
    # Save the image
    cv2.imwrite('output/pentagon.jpg', img)

    # Write group number in last quadrant
    while random_quadrant == q1 or random_quadrant == q2 or random_quadrant == q3:
        random_quadrant = quadrants[np.random.randint(0,4)]

    x1, y1, x2, y2 = random_quadrant
    max_x = x2 - 150
    max_y = y2 - 20
    min_x = x1 + 0
    min_y = y1 + 20

    # Randomly select a point in the quadrant so that the text fits
    text_x = np.random.randint(min_x, max_x)
    text_y = np.random.randint(min_y, max_y)

    # Set font
    font = cv2.FONT_HERSHEY_SIMPLEX = 0

    # Write group number
    cv2.putText(img, 'Group 31', (text_x, text_y), font, 1, (0, 255, 0), 4, cv2.LINE_AA)

    # Save the image
    cv2.imwrite('output/w3q1.jpg', img)

    ### END OF STUDENT CODE ####
    ############################

