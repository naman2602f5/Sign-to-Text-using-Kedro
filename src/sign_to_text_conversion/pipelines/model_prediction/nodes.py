"""
This is a boilerplate pipeline 'model_prediction'
generated using Kedro 0.19.8
"""
import pickle
from PIL import Image
import numpy as np


def load_and_preprocess_image(img_path, target_size=(64, 64)):
    img = Image.open(img_path).convert('L')
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=-1)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

def predict(final_model, image_path):
    img_array = load_and_preprocess_image(image_path, target_size=(128, 128))
    predictions = final_model.predict(img_array)
    print(predictions)
