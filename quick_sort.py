import cv2
import numpy as np
import random

def scale_to_fit(image, max_width=1920, max_height=1080):
    #used for scaling so that the image isn't blown up too wide
    h, w = image.shape[:2]
    scale = min(max_width / w, max_height / h)
    new_size = (int(w * scale), int(h * scale))
    #Resizes an image to a specified width and height. The interpolation method cv2.INTER_AREA is used for downscaling images as it uses pixel area relation, providing high-quality results. - https://learnopencv.com/image-resizing-with-opencv/
    return cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)

def partition(arr, low, high, img_dict, img_win, delay):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

            #update the displayed image
            updated_image = np.hstack([img_dict[index] for index in arr])
            scaled_image = scale_to_fit(updated_image)  # Scale to fit screen
            cv2.imshow(img_win, scaled_image)

            if cv2.waitKey(delay) == 27:  #escape key to break early
                return i

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Update the displayed image
    updated_image = np.hstack([img_dict[index] for index in arr])
    scaled_image = scale_to_fit(updated_image)  # Scale to fit screen
    cv2.imshow(img_win, scaled_image)

    if cv2.waitKey(delay) == 27:  #escape key to break early
        return i + 1

    return i + 1

def quick_sort(arr, low, high, img_dict, img_win, delay):
    if low < high:
        #pass all required arguments to partition
        pi = partition(arr, low, high, img_dict, img_win, delay)

        #recursive calls
        quick_sort(arr, low, pi - 1, img_dict, img_win, delay)
        quick_sort(arr, pi + 1, high, img_dict, img_win, delay)





