import os
import tempfile

from matplotlib import pyplot as plt
import numpy as np
import tensorflow as tf
from PIL import Image
#Загрузка изображения
Image  = tf.keras.preprocessing.image.load_img('1.jpg')
#Преобразование в массив
array = tf.keras.preprocessing.image.img_to_array(Image)


#Преобразование в изображение
Image  = tf.keras.preprocessing.image.array_to_img(array)


#Вывод


Image.save('new' + ".jpg", "JPEG")