import tensorflow as tf
from tensorflow import keras
import cv2
from keras.models import Sequential, Model
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout, BatchNormalization, Activation, \
    GlobalMaxPooling2D
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
import matplotlib.pyplot as plt
import numpy as np

# Image Height and Width for Model
width, height = 86, 86

# Preparing Image for Use in Model as image need to be preprocessed before use.
def prepareImage(filepath):
    # use keras to process the image
    image_after_processing = keras.preprocessing.image.load_img(filepath, target_size=(height, width))
    # image is now added to array so it can be passed into model.
    image_array = keras.preprocessing.image.img_to_array(image_after_processing)
    # create object to be passed into model
    batchimage = np.expand_dims(image_array, axis=0)
    
    return batchimage


# categories for a nice printout of predict.
categories = ["Open", "Closed"]

# load model with keras.load
model = keras.models.load_model('eyes.h5')

# Images from the dataset used to train model
OPEN_EYE_FILE = 'input/test/Open_Eyes/s0012_04796_0_0_1_0_0_03.png'
CLOSED_EYE_FILE = 'input/test/Closed_Eyes/s0016_00015_1_0_0_0_1_01.png'

# My Images from webcam
MY_EYE_OPEN_FILE = 'img/image1.jpg'
MY_EYE_CLOSED_FILE = 'img/image216.jpg'

# call prepare image function to prep images for model.
preparedImage = prepareImage(MY_EYE_OPEN_FILE)

# call model.predict to use model prediction
output = model.predict(preparedImage)

# print output
print("The Eye in This Image is " + str(categories[int(output[0][0])]) + '\n')
print(int(output[0][0]))
