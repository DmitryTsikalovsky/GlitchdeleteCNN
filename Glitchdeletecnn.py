
from keras.preprocessing.image import array_to_img
import loadmodule
import tensorflow as tf
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from tkinter import filedialog
from matplotlib import pyplot as plt
import pandas as pd
import os
import savemodule

test = loadmodule.load()

#images = np.load('gray_scale.npy')
#image1 = images[0][1]
#mainimage = tf.keras.preprocessing.image.array_to_img(image1)
#Image = tf.keras.preprocessing.image.array_to_img(test)

savemodule.saveimage(test)