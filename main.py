import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
from quick_sort import quick_sort, scale_to_fit
import random
from merge_sort import merge_sort

#sort image array using the selected algorithm
#def sort_image(image_array, algorithm):
 #   flat_array = image_array.flatten()
 #   if algorithm == "MergeSort":
#        merge_sort(flat_array)
#    elif algorithm == "QuickSort":
#        flat_array = quick_sort(list(flat_array))
        #reshape array
#    return flat_array.reshape(image_array.shape)


#main gui class
class ImageSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Sorting Application")
        self.image_path = None
        self.original_image = None
        self.image_array = None

        #gui elements
        self.label = tk.Label(self.root, text="Image Sorting Application", font=("Arial", 16))
        self.label.pack(pady=10)
        self.select_button = tk.Button(self.root, text="Select Image", command=self.load_image)
        self.select_button.pack(pady=5)

        #sorting buttons
        self.mergesort_button = tk.Button(self.root, text="Use Merge Sort",
        command=lambda: self.sort_and_display("MergeSort"))
        self.mergesort_button.pack(pady=5)

        self.quicksort_button = tk.Button(self.root, text="Use Quick Sort", command=lambda: self.sort_and_display("QuickSort"))
        self.quicksort_button.pack(pady=5)

    def load_image(self):
        #open dialog
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if not file_path: return
        self.image_path = file_path
        self.original_image = Image.open(self.image_path)
        self.image_array = np.array(self.original_image)
        #image load worked
        messagebox.showinfo("Image Loaded", "Image has been successfully loaded!")

    #this function isnt working rn
    def sort_and_display(self, algorithm):
        if self.image_array == None:
            messagebox.showerror("Error", "No image loaded! Please select an image first.")
            return
        #put syeds code here for scrambling the image and then add sort_image function call. MAKE SURE TO DISPLAY UNSORTED IMAGE FIRST
        # read the image and save it and then the .image function from the numpy library gets the height and width in pixels
        image = cv2.imread("gator.png")
        if image is None:
            print("Error: Unable to load image. Please check the file path.")
            exit(1)

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
        shuffled_img_scaled = scale_to_fit(shuffled_img)  # Scale the shuffled image
        # This displays the shuffled image in a window called image and waits for a key to be pressed
        cv2.imshow('image', shuffled_img_scaled)
        cv2.waitKey(0)

        # sorted_img = shuffled_img.copy()
        if algorithm == "QuickSort":
            quick_sort(index_list, 0, len(index_list) - 1, column_slices, 'image', 1)
        else:
            merge_sort(index_list, 0, len(index_list) - 1, column_slices, 'image', 1)

        sorted_img = np.hstack([column_slices[index] for index in index_list])
        sorted_img_scaled = scale_to_fit(sorted_img)  # Scale the sorted image

        cv2.imshow('image', sorted_img)

        cv2.waitKey(0)

        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSorterApp(root)
    root.mainloop()
