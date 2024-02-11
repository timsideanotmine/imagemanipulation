
# standard imports
import os 
import datetime
import sys

# import packages
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def main():

    """ Bootstrap part of this module """

    default_image = 'kittycat_blebleble.png'
    # default_image = 'kittycat_waaah.png'
    # default_image = 'elon_star_wars.png'
    # default_image = 'no_testing_just_debugging.png'
    # default_image = 'wait_let_me_check_my_messages.png'
    # default_image = 'Awake_but_at_what_cost.png'
    
    default_image_path = os.path.join('..','images','input',default_image)
    use_this_image = np.array(Image.open(default_image_path))
    
    # save_image_path = os.path.join('images','output','kittycat_blebleble_')
    save_image_path = ""

    #random_instructions_list = generate_random_instruction_list_by_plotting_it()
    create_colorful_big_one_by_plotting_it(use_this_image, generate_random_instruction_list_by_plotting_it(), save_image_path)

    return

# ----------------------------------------------------------------
def color_the_image(given_image, color):

    """ This function will turn an image into the given color """
    
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

    """ This function will flip an image horizontally or vertically according to the given manner_of_flip """

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

    """ This function will rotate an image according to the manner_of_rotation """

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

    """ This function will make an image according to the process requested """
    
    if process == "noisy":
        lower_band = 0
        upper_band = 125
        height,width = given_image.shape[:2] 
        given_image[:,:,0] += np.random.randint(lower_band, upper_band, (height, width), dtype = 'uint8')
        given_image[:,:,1] += np.random.randint(lower_band, upper_band, (height, width), dtype = 'uint8')
        given_image[:,:,2] += np.random.randint(lower_band, upper_band, (height, width), dtype = 'uint8')
        return given_image
    
    # elif process == "grainy_making":
    #     given_image = given_image[::10, ::10, :]
    #     return given_image
    
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
def create_colorful_big_one_by_plotting_it(given_image, instruction_list, save_image_path):

    """ This function will draw the colorful_big_one image
        and will save it each time it is randomly composed in 
        folder /images/output with a date/time stamp on it. """

    # set basic parameters for the resulting image  
    rows = 12
    columns = 12
    grid_position = 0 
    title_color = 'black'
    row_original_image = 0
    column_original_image = 0
    grid_position_original_image = 0
    plt.figure(figsize=(36, 48))

    print(f"** step 3 ** Creating each image and subplot the modified sub-image on its gridposition")
    print(f"** step 3 ** Sit back and relax, this might take some time")
    for row in range(1,rows+1):
        for column in range(1,columns+1):

            # load original image
            part_of_colorful_big_one = given_image.copy()

            # prepare clarifying text for each image in the grid
            grid_position +=1
            plt.subplot(rows, columns, grid_position)
            plt.axis('off')
            titel=instruction_list[grid_position-1][0] + '\n' + instruction_list[grid_position-1][1] + '\n' + instruction_list[grid_position-1][2] + '\n' + instruction_list[grid_position-1][3] + '\n' 
            if (instruction_list[grid_position-1][0] == 'no_color' and 
                instruction_list[grid_position-1][1] == 'no_flip' and
                instruction_list[grid_position-1][2] == 'no_rotation' and
                instruction_list[grid_position-1][3] == 'no_making'):
                title_color = 'red'
                row_original_image = row
                column_original_image = column
                grid_position_original_image = grid_position
            else:
                title_color = 'black'

            plt.title(titel, color=title_color)

            # process the nth image with its destined 4 instructions
            part_of_colorful_big_one = create_instructed_image_by_plotting_it(part_of_colorful_big_one, instruction_list[grid_position-1])
            if instruction_list[grid_position-1][3] == "black_and_white":
                plt.imshow(part_of_colorful_big_one, cmap=plt.cm.gray)    
            else:
                plt.imshow(part_of_colorful_big_one)

            # reporting as to how far the process has evolved    
            print(f"** step 3 ** Instruction for grid position {grid_position} was processed", end='\r')
                        
    print()
    print(f"** step 3 ** Original image with red colored title is on row {row_original_image}, column {column_original_image}, grid postion {grid_position_original_image}")
    print()

    if save_image_path != "":
        save_the_image(save_image_path)
    else:
        print(f"** step 4 ** Saving was not requested, no saving done \n")            

    # showing the result on screen
    print(f"** step 5 ** Executing the plt.show() instruction .. yep, still busy ...  \n")
    #plt.title(given_image)
    #plt.title(main().given_image)
    plt.show()
    plt.close
   
    print(f"** step 6 ** All done, do you like the result ? \n")

# ----------------------------------------------------------------  
def create_colorful_big_one_by_numpying_it(given_image, given_grid_instruction_matrix, given_grid_instruction_matrix_configuration):
    pass

# ----------------------------------------------------------------  
def set_grid_instruction_matrix(given_grid_instruction_matrix_configuration):
    
    """ this function will create the necessary 
        test proof images to be show as result of the 
        test Tim made up 
        
        possible instructions overview

        color_the_image(no_color)
        color_the_image(to_blue)
        color_the_image(to_red)
        color_the_image(to_green)

        flip_the_image((no_flip)
        flip_the_image((horizontally)
        flip_the_image((vertically)
        flip_the_image((h_and_v_flip)


        """
    
    if given_grid_instruction_matrix_configuration == "tims_test_1":

        grid_instruction_matrix_width = 8
        grid_instruction_matrix_height = 3
        grid_instruction_matrix = np.empty(
                            (grid_instruction_matrix_height, 
                             grid_instruction_matrix_width), 
                            dtype='U40'
                            )
        
        grid_instruction_matrix = np.full(
                            grid_instruction_matrix.shape,
                            "color_the_image(no_color)"     
                            )           

        return grid_instruction_matrix
    
    elif given_grid_instruction_matrix_configuration == "tims_test_2":

        grid_instruction_matrix_width = 6
        grid_instruction_matrix_height = 4
        grid_instruction_matrix = np.empty(
                            (grid_instruction_matrix_height, 
                             grid_instruction_matrix_width), 
                            dtype='U40'
                            )
        
        grid_instruction_matrix[0,:] = "flip_the_image(no_flip)"
        grid_instruction_matrix[1,:] = "flip_the_image(horizontally)"
        grid_instruction_matrix[2,:] = "flip_the_image(vertically)"
        grid_instruction_matrix[3,:] = "flip_the_image(h_and_v_flip)"

        return grid_instruction_matrix

    elif given_grid_instruction_matrix_configuration == "tims_test_3":

        grid_instruction_matrix_width = 4
        grid_instruction_matrix_height = 4
        grid_instruction_matrix = np.empty(
                            (grid_instruction_matrix_height, 
                             grid_instruction_matrix_width), 
                            dtype='U40'
                            )
        
        grid_instruction_matrix[0,:] = "color_the_image(to_blue)"
        grid_instruction_matrix[1,0] = "color_the_image(to_red)"
        grid_instruction_matrix[1,3] = "color_the_image(to_red)"
        grid_instruction_matrix[2,0] = "color_the_image(to_red)"
        grid_instruction_matrix[2,3] = "color_the_image(to_red)"
        grid_instruction_matrix[3,:] = "color_the_image(to_green)"
        
        return grid_instruction_matrix
            
    # elif given_grid_instruction_matrix_configuration == "johans_extra_1":
    #     return grid_instruction_matrix
    
    # elif given_grid_instruction_matrix_configuration == "johans_extra_2":
    #     return grid_instruction_matrix
    
    
    else:
        # no correct grid_instruction_matrix_configuration was given
        print(f"** WARNING ** incorrect grid_instruction_matrix_configuration '{given_grid_instruction_matrix_configuration}', was given  \n")   
        grid_instruction_matrix_width = 2
        grid_instruction_matrix_height = 2
        grid_instruction_matrix = np.empty(
                            (grid_instruction_matrix_height, 
                             grid_instruction_matrix_width), 
                            dtype='U40'
                            )
        
        grid_instruction_matrix[:,:] = "incorrect configuration"

        return grid_instruction_matrix
    
# ----------------------------------------------------------------  
def save_the_image(save_image_path):

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
    
# ----------------------------------------------------------------  
def create_instructed_image_by_plotting_it(given_image, instruction):

    """ This function will apply the instruction given on a given image.  

        A single instruction is composed of 4 possible image processing options
        in the predefined order as given hereunder :
        
        [color, manner_of_flip, manner_of_rotation, process]
        
        color                     : set color of image to red, green, blue or no color
        color options             : "no_color", "to_red", "to_green", "to_blue"
        
        manner_of_flip            : do a horizontal or vertical flip or do no flip with the image
        manner_of flip options    : "no_flip", "horizontally", "vertically"

        manner_of_rotation        : do a left or right rotation or do no rotation with the image
        manner_of_rtation options : "no_rotation", "to_the_left", "to_the_right"
        
        process                   : apply the process of making the image noisy, shady, black and white or do nothing
        process options           : "no_making", "noisy", "black_and_white", "shady", "double_size"
        
        please note the process of making an image black and white is not regarded 
        as setting a color, but rather as removing the color from an image. That means
        an image can be colorized first but end up being made black_and_whtite
        
        please also note that a horizontal flip and a left rotation produces the same
        result as a vertical flip with a right rotation"""
    
    given_image = color_the_image(given_image, instruction[0])
    given_image = flip_the_image(given_image, instruction[1])
    given_image = rotate_the_image(given_image, instruction[2])
    given_image = make_the_image(given_image, instruction[3])
    
    return given_image
  
# ----------------------------------------------------------------    
def generate_random_instruction_list_by_plotting_it():

    """ This functon creates a list of 144 instructions and then randomizes it.
        
        Please note an instruction is a list of 4 possible image processing options
        An instruction list is thus a list of lists
        
        please note the process option "double_size" is not used in the randomisation function"""
    
    colors = ["no_color", "to_red", "to_green", "to_blue"]
    flips = ["no_flip", "horizontally", "vertically"]
    rotations = ["no_rotation", "to_the_left", "to_the_right"]
    makings = ["no_making", "noisy", "black_and_white", "shady"]

    # 4 possible color options
    # 3 possible flip options 
    # 3 possible rotation options
    # 4 possible process options
    # gives a total of 4 * 3 * 3 * 4 = 144
    number_of_combinations = 144
    
    print(f"** step 1 ** Generating standard combination instruction list of {number_of_combinations} possible combinations", end='\r')
    reference_list = []
    for color in colors:
        for flip in flips:
            for rotation in rotations:
                for making in makings:
                    reference_list.append([color, flip, rotation, making])
    print(f"** step 1 ** Generating standard combination instruction list of {number_of_combinations} possible combinations, done")
    print()
        
    # at this point we will randomize each differentiated combinations of options to have a random sequence of processing into the colorful_big_one image
    print(f"** step 2 ** Randomizing the standard combination list for {number_of_combinations} combinations to create an new image each time executed", end='\r')
    random_sequence = np.random.permutation(np.arange(0, number_of_combinations))
   
    instruction_list = []
    for number in random_sequence:
        instruction_list.append(reference_list[number])

    
    print(f"** step 2 ** Randomizing the standard combination list for {number_of_combinations} combinations to create an new image each time executed, done")
    print()
    return instruction_list 

# ----------------------------------------------------------------
if __name__ == "__main__":
    main()
