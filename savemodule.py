from keras.preprocessing.image import array_to_img
import tensorflow as tf
def save_image(img):
    image = tf.keras.preprocessing.image.array_to_img(img)
    save_path = input("Write your path to save (like D:\\foldername):")
    image.save(save_path +'\glitchdelete.jpg', 'JPEG')
    print('successfully saved in ' + save_path +'\nImage name: glitchdelete.jpg')