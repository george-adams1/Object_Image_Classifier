from PIL import Image
import os

def image_modifier():
    directory = r'C:\Users\georg\OneDrive\Desktop\Desktop\All My Files\Coding Projects\NeuralNetworks\images'
    for filename in os.listdir(directory):
        image = Image.open(f'images/{filename}')
        new_image = image.resize((32,32))
        new_image.save(f'modified_images/{filename}')
        print(image.size)
        print(new_image.size)