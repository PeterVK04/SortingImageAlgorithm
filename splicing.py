import cv2
import numpy as np
import random
import time

# Yo never use time sleep it will die
def bubbleSort(arr, image_arr, img_dict, img_win, delay=1):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                # Update the displayed image
                updated_image = np.hstack([img_dict[index] for index in arr])
                image_arr[:] = updated_image  # Update in place
                cv2.imshow(img_win, image_arr)

                # Use cv2.waitKey for better integration with OpenCV
                if cv2.waitKey(delay) == 27:  # Escape key to break early
                    return

        if not swapped:  # Exit if no swaps occurred in this pass
            break

# Read the image and save it and then the .image function from the numpy library gets the height and width in pixels
image = cv2.imread("wave.jpeg")
height, width, _ = image.shape

# This creates a dictionary where each key represents a column index
# each value is an array of arrays of the rgb col values
column_slices = {i: image[:, i] for i in range(width)}

# This takes the keys of the dictionary and puts them into a list
index_list = list(column_slices.keys())

# This randomizes the indices for each column index of the image
random.shuffle(index_list)

# This uses hstack to combine columns together from the dictionary of column slices
# It loops through each index in the random index list and then takes the column value from the corresponding
# key in the dictionary and then horizontally combines them into a 2d array to represent the shuffled image
shuffled_img = np.hstack([column_slices[index] for index in index_list])

# This displays the shuffled image in a window called image and waits for a key to be pressed
cv2.imshow('image', shuffled_img)
cv2.waitKey(0)


sorted_img = shuffled_img.copy()

bubbleSort(index_list, sorted_img,column_slices,'image', delay=1)

#sorted_img = np.hstack([column_slices[index] for index in indices])


cv2.imshow('image', sorted_img)

cv2.waitKey(0)

cv2.destroyAllWindows()
