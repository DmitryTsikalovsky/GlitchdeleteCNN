import tkinter as tk
import tensorflow as tf
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from tkinter import filedialog

def load():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    Image = tf.keras.preprocessing.image.load_img(file_path)
    input_array = img_to_array(Image)
    return input_array