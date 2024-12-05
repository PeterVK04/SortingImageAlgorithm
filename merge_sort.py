import cv2
import numpy as np
import random


# Merging portion of merge sort algorithm
def merge(arr, start, mid, end, image_arr, img_dict, img_win, delay):
    # Pointer to keep track of element in second half of array
    start2 = mid + 1

    # If the direct merge is already sorted
    if arr[mid] <= arr[start2]:
        return

    # Two pointers to maintain start of both arrays to merge
    while start <= mid and start2 <= end:

        # If the elements at start index and start2 index are in the right order
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            # Shift all the elements from start index to start2 - 1 index to the right by 1
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            # Move element at start2 index to start index
            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1

            # Update the displayed image
            updated_image = np.hstack([img_dict[index] for index in arr])
            image_arr[:] = updated_image  # Update in place
            cv2.imshow(img_win, image_arr)

            # Use cv2.waitKey for better integration with OpenCV
            if cv2.waitKey(delay) == 27:  # Escape key to break early
                return


# In-Place Merge Sort Algorithm
def merge_sort(arr, left, right, image_arr, img_dict, img_win, delay):
    if left < right:
        # Same as (left + right) / 2, but avoids overflow for large left and right
        mid = left + (right - left) // 2

        # Split the first and second halves of arr into subarrays
        merge_sort(arr, left, mid, image_arr, img_dict, img_win, delay)
        merge_sort(arr, mid + 1, right, image_arr, img_dict, img_win, delay)

        # Merge the sorted subarrays together
        merge(arr, left, mid, right, image_arr, img_dict, img_win, delay)


# Read the image and save it and then the .image function from the numpy library gets the height and width in pixels
image = cv2.imread("../gator.png")
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

merge_sort(index_list, 0, len(index_list) - 1, sorted_img, column_slices,'image', 1)


cv2.imshow('image', sorted_img)

cv2.waitKey(0)

cv2.destroyAllWindows()
