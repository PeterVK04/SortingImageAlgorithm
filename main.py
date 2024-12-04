import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np


def merge_sort(array):
    #put iterative merge sort call here
    x = 5  # placeholder for now


def quick_sort(array):
    #put iterative quick sort call here
    x = 5  # placeholder for now


#sort image array using the selected algorithm
def sort_image(image_array, algorithm):
    flat_array = image_array.flatten()
    if algorithm == "MergeSort":
        merge_sort(flat_array)
    elif algorithm == "QuickSort":
        flat_array = quick_sort(list(flat_array))
        #reshape array
    return flat_array.reshape(image_array.shape)


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

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSorterApp(root)
    root.mainloop()
