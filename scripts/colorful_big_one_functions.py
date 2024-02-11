# standard imports
import os 
import datetime
import sys

# import packages
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ----------------------------------------------------------------
def color_the_image(given_image, color):

    """ 
    This function will turn an image into the given color 
    
    Parameters:

    given_image
    image_array(numpy.ndarray): a 3d array representing an image
        array shape is (height, width, channels)
        height: in number of pixels
        width: in number of pixels
        channels: 3, RGB images only

    color (instruction)
    string type: non recognized values will do nothing
        valid values:
        'to_red': will turn image red
        'to_blue': will turn image blue
        'to_green': will turn image green
        <any other text>: will not change the given image/ndarray

    Returns:
        will return the given image/ndarray but changed 
        to its respective instruction
    
    Example:
    >>> import colorful_big_one_functions as cbof
    >>> image_to_show = cbof.color_the_image(given_image, 'to_blue')
    
    """
    
    if color == "to_red":
        given_image[:,:,[1,2]] = 0
        return given_image
    
    elif color == "to_blue":
        given_image[:,:,[0,1]] = 0
        return given_image
    
    elif color == "to_green":
        given_image[:,:,[0,2]] = 0
        return given_image
    
    else:
        # "no_color or faulty color"
        return given_image

# ----------------------------------------------------------------    
def flip_the_image(given_image, manner_of_flip):

    """ 
    This function will flip an image horizontally or vertically 
    according to the given manner_of_flip 
    
    Parameters:

    given_image
    image_array(numpy.ndarray): a 3d array representing an image
        array shape is (height, width, channels)
        height: in number of pixels
        width: in number of pixels
        channels: 3, RGB images only

    manner_of_flip (instruction)
    string type: non recognized values will do nothing
        valid values:
        'horizontally': will do a mirror flip horizontally
        'vertically': will do a vertical mirror flip
        <any other text>: will not change the given image/ndarray

    Returns:
        will return the given image/ndarray but changed 
        to its respective instruction
    
    Example:
    >>> import colorful_big_one_functions as cbof
    >>> image_to_show = cbof.flip_the_image(given_image, 'vertically')
    
    """

    if manner_of_flip == "horizontally":
        given_image = np.fliplr(given_image)
        return given_image
    
    elif manner_of_flip == "vertically":
        given_image = flip_the_image(given_image, "horizontally")
        given_image = rotate_the_image(given_image, "to_the_left")
        given_image = rotate_the_image(given_image, "to_the_left")
        return given_image

    else:
        # "no_flip or faulty manner_of_flip"
        return given_image
    
# ----------------------------------------------------------------
def rotate_the_image(given_image, manner_of_rotation):

    """ 
    This function will rotate an image according to the manner_of_rotation 
    
    Parameters:

    given_image
    image_array(numpy.ndarray): a 3d array representing an image
        array shape is (height, width, channels)
        height: in number of pixels
        width: in number of pixels
        channels: 3, RGB images only

    manner_of_rotation (instruction)
    string type: non recognized values will do nothing
        valid values:
        'to_the_left': will rotate the image 90° to the left
        'to_the_right': will rotate the image 90° to the right
        <any other text>: will not change the given image/ndarray

    Returns:
        will return the given image/ndarray but changed 
        to its respective instruction
    
    Example:
    >>> import colorful_big_one_functions as cbof
    >>> image_to_show = cbof.rotate_the_image(given_image, 'to_the_right')
    
    """

    if manner_of_rotation == "to_the_left":
        given_image = np.rot90(given_image)
        return given_image
    
    elif manner_of_rotation == "to_the_right":
        given_image = np.rot90(given_image, 3)
        return given_image

    else:
        # "no_rotation or faulty rotation"
        return given_image
    
# ----------------------------------------------------------------
def make_the_image(given_image, process):

    """ 
    This function will make an image according to the process requested 
    
    Parameters:

    given_image
    image_array(numpy.ndarray): a 3d array representing an image
        array shape is (height, width, channels)
        height: in number of pixels
        width: in number of pixels
        channels: 3, RGB images only

    process (instruction)
    string type: non recognized values will do nothing
        valid values:
        'noisy': will make the image noisy
        'black_and_white': will make the image black an white (only with plt.imshow(given_image, cmap=plt.cm.gray)
        'shady': will top off color values over 150 to make shady
        'double_size': will double the pixel size of the image
        'grayscale': will grayscale the colors of the image (only with plt.imshow(given_image, cmap=plt.cm.gray)
        'grainy': will make grainy by limiting image to 1/10th of the information
        'inverted': will inverted by doing 255 - value of color
        'sepia_tone': will render the image old as fuck
        'solarized': will show subject in image to look baked
        'posterized': will render the image famous
        'twirled': will make you look twice at the result
        'rippled': will make you feel sinus suicidal
        'swirled': will mmake you feel seasick
        <any other text>: will not change the given image/ndarray

    Returns:
        will return the given image/ndarray but changed 
        to its respective instruction
    
    Example:
    >>> import colorful_big_one_functions as cbof
    >>> image_to_show = cbof.make_the_image(given_image, 'sepia_tone')
    
    """
    
    if process == "noisy":
        lower_band = 0
        upper_band = 125
        height,width = given_image.shape[:2] 
        given_image[:,:,0] += np.random.randint(lower_band, upper_band, (height, width), dtype = 'uint8')
        given_image[:,:,1] += np.random.randint(lower_band, upper_band, (height, width), dtype = 'uint8')
        given_image[:,:,2] += np.random.randint(lower_band, upper_band, (height, width), dtype = 'uint8')
        return given_image
    
    # this setting can only be used with plt.imshow(part_of_colorful_big_one, cmap=plt.cm.gray)    
    elif process == "black_and_white":    
        given_image = given_image.astype(float)
        given_image = given_image.sum(axis = 2)
        given_image /= given_image.max()
        given_image = np.absolute(given_image)
        return given_image
    
    elif process == "shady":       
        given_image = np.where(given_image > 150, 150 , 20)
        return given_image
    
    elif process == "double_size":
        height, width, channels = given_image.shape
        factor = 2
        #  initialize the factor 2 image
        given_image_doubled = np.zeros((height * factor, width * factor, channels), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                for c in range(channels):
                    given_image_doubled[i*factor, j*factor, c] = given_image[i, j, c]
                    given_image_doubled[i*factor+1, j*factor, c] = given_image[i, j, c]
                    given_image_doubled[i*factor, j*factor+1, c] = given_image[i, j, c]
                    given_image_doubled[i*factor+1, j*factor+1, c] = given_image[i, j, c]
        return given_image_doubled        

    # this setting can only be used with plt.imshow(part_of_colorful_big_one, cmap=plt.cm.gray)    
    elif process == "grayscale":
        given_image = np.mean(given_image, axis=2, dtype=np.uint8)
        return given_image
    
    elif process == "grainy":
        given_image = given_image[::10, ::10, :]
        return given_image
    
    elif process == "inverted":    
        given_image = 255 - given_image
        return given_image
    
    elif process == "sepia_tone":       
        sepia_matrix = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])
        given_image = np.dot(given_image, sepia_matrix.T)
        given_image = np.clip(given_image, 0, 255).astype(np.uint8)
        return given_image
    
    elif process == "solarized":
        threshold = 128
        given_image = np.where(given_image < threshold, given_image, 255 - given_image)
        return given_image        

    elif process == "posterized":
        levels = 4
        given_image = given_image // (256 // levels) * (256 // levels)
        return given_image        

    elif process == "twirled":
        height, width, _ = given_image.shape
        center = (width // 2, height // 2)
        radius = 250
        angle = 2
        y, x = np.ogrid[:height, :width]
        x -= center[0]
        y -= center[1]
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x) + angle * np.exp(-(r / radius)**2)
        new_x = (center[0] + r * np.cos(theta)).clip(0, width - 1).astype(int)
        new_y = (center[1] + r * np.sin(theta)).clip(0, height - 1).astype(int)
        distorted_image = given_image[new_y, new_x]
        return distorted_image

    elif process == "mosaic":
        block_size = (30, 30)
        height, width, _ = given_image.shape
        block_height, block_width = block_size
        new_height = height // block_height
        new_width = width // block_width
        mosaic_image = given_image[:new_height * block_height, :new_width * block_width]
        mosaic_image = mosaic_image.reshape((new_height, block_height, new_width, block_width, 3))
        return mosaic_image.mean(axis=(1, 3)).astype(np.uint8)
      
    elif process == "rippled":
        amplitude = 10
        frequency = 25
        height, width, _ = given_image.shape
        y, x = np.ogrid[:height, :width]
        distorted_y = y + amplitude * np.sin(2 * np.pi * x / frequency)
        distorted_x = x + amplitude * np.sin(2 * np.pi * y / frequency)
        distorted_image = given_image[distorted_y.astype(int) % height, distorted_x.astype(int) % width]
        return distorted_image
     
    elif process == "swirled":
        strength = 0.0025
        height, width, _ = given_image.shape
        center = (width // 2, height // 2)
        y, x = np.ogrid[:height, :width]
        x -= center[0]
        y -= center[1]
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x) + strength * r
        new_x = (center[0] + r * np.cos(theta)).clip(0, width - 1).astype(int)
        new_y = (center[1] + r * np.sin(theta)).clip(0, height - 1).astype(int)
        distorted_image = given_image[new_y, new_x]
        return distorted_image


    else:
        # "no_making or faulty making"
        return given_image    
    
# ----------------------------------------------------------------    
def show_the_image(image_to_show):

    """
    
    Just showing things, nothing more
    
    """

    plt.figure(figsize=(36, 48))
    plt.axis('off')
    plt.imshow(image_to_show)
    plt.show()
    plt.close

    return

# ----------------------------------------------------------------  
def save_the_image(save_image_path):

    """
    
    Just saving things, nothing more
    
    """

    # saving the image with datetime stamp
    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.strftime("%Y%m%d_%H%M%S")
    filename = save_image_path + timestamp + ".png"
    # save_image_path = os.path.join('..', 'images','output', filename)
    # save_image_path = os.path.join('images','output', filename)
    save_image_path = os.path.join(filename)
    print(f"** step 4 ** Saving the resulting colorful_big_one image as {save_image_path} \n")
    # print(sys.path)
    # print(f"** step 4 ** Saving the resulting colorful_big_one image as {save_image_path} \n")
    plt.savefig(save_image_path, format="png")

        