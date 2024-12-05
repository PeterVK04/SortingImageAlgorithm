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