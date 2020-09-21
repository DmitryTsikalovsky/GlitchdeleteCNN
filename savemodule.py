from PIL import Image
from keras.preprocessing.image import array_to_img
import tensorflow as tf
def saveimage(img):
    Image = tf.keras.preprocessing.image.array_to_img(img)
    path = input("Write your path to save (like D:\\foldername):")
    Image.save(path +'\glitchdelete.jpg', 'JPEG')
    print('successfully saved in ' + path +'\nImage name: glitchdelete.jpg')