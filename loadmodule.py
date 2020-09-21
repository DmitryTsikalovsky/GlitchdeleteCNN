import tkinter as tk
import tensorflow as tf
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from tkinter import filedialog

def load_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    input_image = tf.keras.preprocessing.image.load_img(file_path)
    input_image_array = img_to_array(input_image)
    return input_image_array