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

train_dir = './input/train'
test_dir = './input/test'

# Image Height and Width for Model
width, height = 86, 86

# Preprocessing of image dataset for training.
training = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1 / 255.0, rotation_range=7, horizontal_flip=True,
                                                           validation_split=0.1
                                                           ).flow_from_directory(train_dir,
                                                                                 class_mode='categorical',
                                                                                 batch_size=8,
                                                                                 target_size=(width, height),
                                                                                 subset="training")
# Preprocessing of image dataset for training.
testing = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1 / 255.0,
                                                          ).flow_from_directory(test_dir,
                                                                                class_mode='categorical',
                                                                                batch_size=8,
                                                                                shuffle=False,
                                                                                target_size=(width, height))
# Preprocessing of image dataset for training.
validating = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1 / 255.0,
                                                             rotation_range=7,
                                                             horizontal_flip=True
                                                             ).flow_from_directory(train_dir,
                                                                                   batch_size=8,
                                                                                   class_mode='categorical',
                                                                                   target_size=(width, height),
                                                                                   subset='validation', shuffle=True)

# Declare Optimiser Adam is a popular optimiser widely used.
optimizer = Adam(lr=0.001, beta_1=0.9, beta_2=0.99, decay=0.001 / 32)

EarlyStop = EarlyStopping(patience=10, restore_best_weights=True)
Reduce_LR = ReduceLROnPlateau(monitor='val_accuracy', verbose=2, factor=0.5, min_lr=0.00001)

# callback is a set of functions to be applied at given stages of the training procedure
callback = [EarlyStop, Reduce_LR]

# Declaring how many categories
num_classes = 2
num_detectors = 32

# Sequential Model
model = Sequential()

# Input Layer
model.add(Conv2D(num_detectors, (3, 3), activation='relu', padding='same', input_shape=(width, height, 3)))

# Layering Model taken from an Image classification project on Kaggle with high percentage accuracy.
model.add(BatchNormalization())

model.add(Conv2D(num_detectors, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization())

model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))

model.add(Conv2D(2 * num_detectors, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization())

model.add(Conv2D(2 * num_detectors, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization())

model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))

model.add(Conv2D(2 * 2 * num_detectors, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization())

model.add(Conv2D(2 * 2 * num_detectors, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization())

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(2 * 2 * 2 * num_detectors, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization())

model.add(Conv2D(2 * 2 * 2 * num_detectors, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization())

model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))

model.add(Flatten())

model.add(Dense(2 * num_detectors, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))

model.add(Dense(2 * num_detectors, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))

# Output Layer
model.add(Dense(num_classes, activation='softmax'))

# compile model
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=["accuracy"])

# print summary of created model
model.summary()

# Estimate val and loss using evaluate model.
val, los = model.evaluate(testing)

# begin training of the model using model.fit function
fitmodel = model.fit(training, validation_data=validating, epochs=10, callbacks=callback, verbose=2)
metrics = fitmodel.fitmodel

# plot information
plt.plot(fitmodel.epoch, metrics['loss'])
plt.legend(['loss'])
plt.show()

# save model for use.
model.save('eyemodel.h5')