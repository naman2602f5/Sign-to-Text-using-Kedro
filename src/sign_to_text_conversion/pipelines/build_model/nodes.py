"""
This is a boilerplate pipeline 'build_model'
generated using Kedro 0.19.8
"""
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def build_model(input_shape):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, padding="same", activation="relu", input_shape=input_shape))
    model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='valid'))
    model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, padding="same", activation="relu"))
    model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='valid'))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(units=128, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.40))
    model.add(tf.keras.layers.Dense(units=96, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.40))
    model.add(tf.keras.layers.Dense(units=64, activation='relu'))
    model.add(tf.keras.layers.Dense(units=27, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model
