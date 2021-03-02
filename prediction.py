from tensorflow.keras import datasets, layers, models
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from ImageResizer import image_modifier
import os

image_modifier()
directory = r'C:\Users\georg\OneDrive\Desktop\Desktop\All My Files\Coding Projects\NeuralNetworks\modified_images'

class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

model = models.load_model('image_classifier.model')
for filename in os.listdir(directory):
    img = cv.imread(f'modified_images/{filename}')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.imshow(img, cmap=plt.cm.binary)

    prediction = model.predict(np.array([img]) / 255)
    index = np.argmax(prediction)
    print(filename)
    print(f'Prediction = {class_names[index]}')