
# standard imports
import os 
import datetime
import sys
import random

# import packages
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# import self made module
current_working_directory = os.getcwd()                   
scripts_directory = os.path.join(current_working_directory, 'scripts') 
# sys.path.remove(scripts_directory)
sys.path.append(scripts_directory)  

import scripts.colorful_big_one_functions as cbof
import scripts.colorful_big_one_solutions as cbos

# change the image (kittycat_blebleble.png) with the available pictures in /input to use another image
# provide your own in the /input folder
# images need to be squared, so need to have the exact same height/width in pixels
loaded_image_path = os.path.join('images','input','awake_but_at_what_cost.png')
use_this_image = np.array(Image.open(loaded_image_path))

# -------------------------------------
# tims_image_1A, tile solution, 1 single image, 8 x 3
# options for given_random_combination : 'default', 'randomize_color', 'randomize_flip', 'randomize_rotate', 'randomize_making'
image_to_show = cbos.create_tims_image_1_by_numpying_it(use_this_image.copy(), 'default')
cbof.show_the_image(image_to_show)
# image_to_show = cbos.create_tims_image_1_by_numpying_it(use_this_image.copy(), 'randomize_color')
# cbof.show_the_image(image_to_show)
# image_to_show = cbos.create_tims_image_1_by_numpying_it(use_this_image.copy(), 'randomize_making')
# cbof.show_the_image(image_to_show)

# -------------------------------------
# # tims_image_2, v/h-stack solution, 4 flipped rows
# options for given_random_combination : 'default', 'randomize_color', 'randomize_making',
# note : the orientations of the exercise are never changed
image_to_show = cbos.create_tims_image_2_by_numpying_it(use_this_image.copy(), 'default')
cbof.show_the_image(image_to_show)
# image_to_show = cbos.create_tims_image_2_by_numpying_it(use_this_image.copy(), 'randomize_color')
# cbof.show_the_image(image_to_show)
# image_to_show = cbos.create_tims_image_2_by_numpying_it(use_this_image.copy(), 'randomize_making')
# cbof.show_the_image(image_to_show)

# -------------------------------------
# # # tims_image_3, clockwise color solution with double sized image
# options for given_random_combination : 'default', 'randomize_flip', 'randomize_rotate', 'randomize_making'
# note : the colors of the exercise are never changed
image_to_show = cbos.create_tims_image_3_by_numpying_it(use_this_image.copy(), 'default')
cbof.show_the_image(image_to_show)
# image_to_show = cbos.create_tims_image_3_by_numpying_it(use_this_image, 'randomize_flip')
# cbof.show_the_image(image_to_show)
# image_to_show = cbos.create_tims_image_3_by_numpying_it(use_this_image, 'randomize_rotate')
# cbof.show_the_image(image_to_show)
# image_to_show = cbos.create_tims_image_3_by_numpying_it(use_this_image, 'randomize_making')
# cbof.show_the_image(image_to_show)

# -------------------------------------
# # johans_image_1, clockwise color solution with double sized image, 4 x 4
# no options for given_random_combination : all is randomized
# note : the framework is fixed, is stacked by np.concatenate 
image_to_show = cbos.create_johans_image_1_by_numpying_it(use_this_image.copy())
cbof.show_the_image(image_to_show)
    