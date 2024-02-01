
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os 
import sys 
import datetime
from scripts import colorful_big_one

print(sys.path)
loaded_image_path = os.path.join('images','input','kittycat_blebleble.png')
use_this_image = np.array(Image.open(loaded_image_path))

instructions = colorful_big_one.generate_random_instruction_list()
colorful_big_one.create_colorful_big_one(use_this_image, instructions)

