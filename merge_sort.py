import cv2
import numpy as np
import random

from quick_sort import scale_to_fit


def wait_for_space():
    while True:
        #32 is ASCII value for space and we use 0xFF to just get the ASCII value for the cv function (because cv will give 32 bits when we only need 8)- https://stackoverflow.com/questions/54454913/why-use-0xff-in-waitkey
        if cv2.waitKey(1) & 0xFF == 32:  #wait for spacebar
            break
        elif cv2.waitKey(1) & 0xFF == 27:  #escape key to exit
            cv2.destroyAllWindows()
            exit()
#merging portion of merge sort algorithm
def merge_sort(arr, start, end, column_slices, img_win, delay):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid, column_slices, img_win, delay)
        merge_sort(arr, mid + 1, end, column_slices, img_win, delay)
        merge(arr, start, mid, end, column_slices, img_win, delay)

def merge(arr, start, mid, end, column_slices, img_win, delay):
    #create temporary arrays
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

    i = j = 0
    k = start

    #merge the temporary arrays back into arr[start..end]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

        #add visualization updates here
        updated_image = np.hstack([column_slices[index] for index in arr])
        scaled_image = scale_to_fit(updated_image)
        cv2.imshow(img_win, scaled_image)
        if cv2.waitKey(delay) == 27:  #escape key to exit
            cv2.destroyAllWindows()
            exit()

    #copy the remaining elements of left[], if any
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

        #add visualization updates here
        updated_image = np.hstack([column_slices[index] for index in arr])
        scaled_image = scale_to_fit(updated_image)
        cv2.imshow(img_win, scaled_image)
        if cv2.waitKey(delay) == 27:
            cv2.destroyAllWindows()
            exit()

    #cpy the remaining elements of right[], if any
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

        #Add visualization updates here
        updated_image = np.hstack([column_slices[index] for index in arr])
        scaled_image = scale_to_fit(updated_image)
        cv2.imshow(img_win, scaled_image)
        if cv2.waitKey(delay) == 27:
            cv2.destroyAllWindows()
            exit()
