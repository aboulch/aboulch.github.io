"""Test program for IOGS TP."""

print("IMPORTS")
print("--> import os and set cpu device")
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""
print("--> import keras")
import keras
from keras.datasets import cifar10, cifar100
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import LSTM, SimpleRNN
print("--> import numpy")
import numpy as np
print("--> import math")
import math
print("--> import matplotlib")
import matplotlib.pyplot as plt
print("--> import scikitlearn")
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

print("TEST KERAS")
print("--> Sequential")
model_seq = Sequential()
model_seq.add(Conv2D(32, (3, 3), padding='same', input_shape=[32, 32, 3]))
model_seq.add(Activation('relu'))
model_seq.add(MaxPooling2D(pool_size=(2, 2)))
model_seq.add(Conv2D(64, (3, 3), padding='same'))
model_seq.add(Activation('relu'))
model_seq.add(MaxPooling2D(pool_size=(2, 2)))
model_seq.add(Flatten())
model_seq.add(Dense(512))
model_seq.add(Activation('relu'))
model_seq.add(Dense(10))
model_seq.add(Activation('softmax'))
model_seq.summary()

x_train = np.zeros((100, 32, 32, 3), dtype=np.float32)
y_train = np.zeros((100, 10), dtype=np.int)
for i in range(100):
    y_train[i, i % 10] = 1
# compile the model
model_seq.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
model_seq.fit(x_train, y_train, batch_size=10, epochs=1, shuffle=True)

print("--> Recurrent")
model = Sequential()
look_back = 3
model.add(SimpleRNN(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
trainX = np.zeros((10, 1, 3))
trainY = np.zeros((10, 1))
model.fit(trainX, trainY, epochs=1, batch_size=1, verbose=2)

print("DONE")
