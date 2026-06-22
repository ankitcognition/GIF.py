import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['image1.jpeg', 'image2.jpeg']

images = []

first = Image.open(filenames[0])
size = first.size

for filename in filenames:
    img = Image.open(filename)
    img = img.resize(size)     
    images.append(np.array(img))

iio.imwrite(
    'GIF',
    images,
    duration=0.5,
    loop=0
)

print("GIF created successfully!")