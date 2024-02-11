# standard imports
import os 
import datetime
import sys
import random

# import packages
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# import own made modules
import colorful_big_one_functions as cbof

# ----------------------------------------------------------------
def main():

    """ 
    
    Main() showcases the main function 
    create_colorful_big_one_by_numpying_it
            
    """

    default_image = 'kittycat_blebleble.png'
    # default_image = 'kittycat_waaah.png'
    # default_image = 'elon_star_wars.png'
    # default_image = 'no_testing_just_debugging.png'
    # default_image = 'wait_let_me_check_my_messages.png'
    # default_image = 'Awake_but_at_what_cost.png'
    
    default_image_path = os.path.join('..','images','input',default_image)
    use_this_image = np.array(Image.open(default_image_path))
    
    # -------------------------------------
    # tims_image_1A, tile solution, 1 single image, 8 x 3
    # options for given_random_combination : 'default', 'randomize_color', 'randomize_flip', 'randomize_rotate', 'randomize_making'
    image_to_show = create_tims_image_1_by_numpying_it(use_this_image.copy(), 'default')
    cbof.show_the_image(image_to_show)
    # image_to_show = cbos.create_tims_image_1_by_numpying_it(use_this_image.copy(), 'randomize_color')
    # cbof.show_the_image(image_to_show)
    # image_to_show = cbos.create_tims_image_1_by_numpying_it(use_this_image.copy(), 'randomize_making')
    # cbof.show_the_image(image_to_show)

    # -------------------------------------
    # # tims_image_2, v/h-stack solution, 4 flipped rows
    # options for given_random_combination : 'default', 'randomize_color', 'randomize_making',
    # note : the orientations of the exercise are never changed
    image_to_show = create_tims_image_2_by_numpying_it(use_this_image.copy(), 'default')
    cbof.show_the_image(image_to_show)
    # image_to_show = cbos.create_tims_image_2_by_numpying_it(use_this_image.copy(), 'randomize_color')
    # cbof.show_the_image(image_to_show)
    # image_to_show = cbos.create_tims_image_2_by_numpying_it(use_this_image.copy(), 'randomize_making')
    # cbof.show_the_image(image_to_show)

    # -------------------------------------
    # # # tims_image_3, clockwise color solution with double sized image
    # options for given_random_combination : 'default', 'randomize_flip', 'randomize_rotate', 'randomize_making'
    # note : the colors of the exercise are never changed
    image_to_show = create_tims_image_3_by_numpying_it(use_this_image, 'default')
    cbof.show_the_image(image_to_show)
    # image_to_show = cbos.create_tims_image_3_by_numpying_it(use_this_image, 'randomize_flip')
    # cbof.show_the_image(image_to_show)
    # image_to_show = cbos.create_tims_image_3_by_numpying_it(use_this_image, 'randomize_rotate')
    # cbof.show_the_image(image_to_show)
    # image_to_show = cbos.create_tims_image_3_by_numpying_it(use_this_image, 'randomize_making')
    # cbof.show_the_image(image_to_show)
    
    return

# ----------------------------------------------------------------  
# Functions <*>_by_numpying_it hereunder only to be used with the function
# create_colorful_big_one_by_numpying_it(given_image, ...)
# ----------------------------------------------------------------
def generate_random_instruction_list_by_numpying_it():

    """ 
    
    This function will generate a single list object with a combination
    of 4 possible functions to be applied to an image

    See further below to check which combinations are possible
    
    """
        
    colors = ["to_red", "to_green", "to_blue"]
    flips = ["horizontally", "vertically"]
    rotations = ["to_the_left", "to_the_right"]
    makings = ["twirled", "rippled", "swirled"]

    instruction_list = []
    instruction_list.append(random.choice(colors))
    instruction_list.append(random.choice(flips))
    instruction_list.append(random.choice(rotations))
    instruction_list.append(random.choice(makings))

    print(instruction_list)
    
    return instruction_list 

# ----------------------------------------------------------------  
def apply_combination_of_functions_by_numpying_it(given_image, given_color, given_manner_of_flip, given_manner_of_rotation, given_process):
    
    """

    This function will apply a combination of functions to a given image
    to provide a variant of the orignal image given in the function

    """

    instruction = generate_random_instruction_list_by_numpying_it()

    if given_color != 'no_color':
        given_image = cbof.color_the_image(given_image, instruction[0])

    if given_manner_of_flip != 'no_flip':
        given_image = cbof.flip_the_image(given_image, instruction[1])

    if given_manner_of_rotation != 'no_rotate':
        given_image = cbof.rotate_the_image(given_image, instruction[2])

    if given_process != 'no_making':
        given_image = cbof.make_the_image(given_image, instruction[3])

    return given_image

# ----------------------------------------------------------------  
def create_tims_image_1_by_numpying_it(given_image, given_random_combination):

    # tims_image_1A, tile solution, 1 single image

    height, width, _ = given_image.shape
    height_factor = 3
    width_factor = 8
    new_height = height * height_factor
    new_width = width * width_factor

    if given_random_combination == 'randomize_color':
        given_image = apply_combination_of_functions_by_numpying_it(given_image, 'any_color', 'no_flip', 'no_rotate', 'no_making')
    elif given_random_combination == 'randomize_flip':
        given_image = apply_combination_of_functions_by_numpying_it(given_image, 'no_color', 'any_flip', 'no_rotate', 'no_making')
    elif given_random_combination == 'randomize_rotate':
        given_image = apply_combination_of_functions_by_numpying_it(given_image, 'no_color', 'no_flip', 'any_rotate', 'no_making')
    elif given_random_combination == 'randomize_making':
        given_image = apply_combination_of_functions_by_numpying_it(given_image, 'no_color', 'no_flip', 'no_rotate', 'any_making')
    
    given_image_to_show = np.tile(given_image, (new_height // given_image.shape[0], new_width // given_image.shape[1], 1))

    # # tims_image_1B, v/h-stack solution, 1 single image
    
    # vstack_factor = 3
    # hstack_factor = 8
    
    # image_stacked_horizontally = np.hstack([use_this_image] * hstack_factor)
    # image_stacked_vertically = np.vstack([image_stacked_horizontally] * vstack_factor)

    return given_image_to_show

# ----------------------------------------------------------------  
def create_tims_image_2_by_numpying_it(given_image, given_random_combination):

    # tims_image_2, v/h-stack solution, 4 flipped rows

    hstack_factor = 6

    # image processing

    given_image_1 = given_image.copy()
    given_image_2 = given_image.copy()
    given_image_3 = given_image.copy()
    given_image_4 = given_image.copy()

    if given_random_combination == 'randomize_color':
        given_image_1 = apply_combination_of_functions_by_numpying_it(given_image_1, 'any_color', 'no_flip', 'no_rotate', 'no_making')
    elif given_random_combination == 'randomize_making':
        given_image_1 = apply_combination_of_functions_by_numpying_it(given_image_1, 'no_color', 'no_flip', 'no_rotate', 'any_making')

    
    if given_random_combination == 'randomize_color':
        given_image_2 = apply_combination_of_functions_by_numpying_it(given_image_2, 'any_color', 'no_flip', 'no_rotate', 'no_making')
    elif given_random_combination == 'randomize_making':
        given_image_2 = apply_combination_of_functions_by_numpying_it(given_image_2, 'no_color', 'no_flip', 'no_rotate', 'any_making')

    
    if given_random_combination == 'randomize_color':
        given_image_3 = apply_combination_of_functions_by_numpying_it(given_image_3, 'any_color', 'no_flip', 'no_rotate', 'no_making')
    elif given_random_combination == 'randomize_making':
        given_image_3 = apply_combination_of_functions_by_numpying_it(given_image_3, 'no_color', 'no_flip', 'no_rotate', 'any_making')

    
    if given_random_combination == 'randomize_color':
        given_image_4 = apply_combination_of_functions_by_numpying_it(given_image_4, 'any_color', 'no_flip', 'no_rotate', 'no_making')
    elif given_random_combination == 'randomize_making':
        given_image_4 = apply_combination_of_functions_by_numpying_it(given_image_4, 'no_color', 'no_flip', 'no_rotate', 'any_making')

    # form processing    
    
    given_image_row_1 = cbof.flip_the_image(given_image_1,'no_flip')
    image_row_1 = np.hstack([given_image_row_1] * hstack_factor)

    given_image_row_2 = cbof.flip_the_image(given_image_2,'horizontally')
    image_row_2 = np.hstack([given_image_row_2] * hstack_factor)

    given_image_row_3 = cbof.flip_the_image(given_image_3,'vertically')
    image_row_3 = np.hstack([given_image_row_3] * hstack_factor)

    given_image_row_4 = cbof.flip_the_image(given_image_4,'horizontally')
    given_image_row_4 = cbof.flip_the_image(given_image_row_4,'vertically')
    image_row_4 = np.hstack([given_image_row_4] * hstack_factor)
    
    given_image_to_show = image_row_1
    given_image_to_show = np.vstack((given_image_to_show, image_row_2))
    given_image_to_show = np.vstack((given_image_to_show, image_row_3))
    given_image_to_show = np.vstack((given_image_to_show, image_row_4))
    
    return given_image_to_show    

# ----------------------------------------------------------------
def create_tims_image_3_by_numpying_it(given_image, given_random_combination):

    # tims_image_3, clockwise color solution with double sized image

    hstack_factor_blue = 4
    hstack_factor_green = 4
    vstack_factor_red = 2

    given_image_top = given_image.copy()
    given_image_bottom = given_image.copy()
    given_image_left_and_right = given_image.copy()
    given_image_center = given_image.copy()

    if given_random_combination == 'randomize_flip':
        given_image_top = apply_combination_of_functions_by_numpying_it(given_image_top, 'no_color', 'any_flip', 'no_rotate', 'no_making')
    elif given_random_combination == 'randomize_rotate':
        given_image_top = apply_combination_of_functions_by_numpying_it(given_image_top, 'no_color', 'no_flip', 'any_rotate', 'no_making')
    elif given_random_combination == 'randomize_making':
        given_image_top = apply_combination_of_functions_by_numpying_it(given_image_top, 'no_color', 'no_flip', 'no_rotate', 'any_making')

    
    if given_random_combination == 'randomize_flip':
        given_image_bottom = apply_combination_of_functions_by_numpying_it(given_image_bottom, 'no_color', 'any_flip', 'no_rotate', 'no_making')
    elif given_random_combination == 'randomize_rotate':
        given_image_bottom = apply_combination_of_functions_by_numpying_it(given_image_bottom, 'no_color', 'no_flip', 'any_rotate', 'no_making')
    elif given_random_combination == 'randomize_making':
        given_image_bottom = apply_combination_of_functions_by_numpying_it(given_image_bottom, 'no_color', 'no_flip', 'no_rotate', 'any_making')

    if given_random_combination == 'randomize_flip':
        given_image_left_and_right = apply_combination_of_functions_by_numpying_it(given_image_left_and_right, 'no_color', 'any_flip', 'no_rotate', 'no_making')
    elif given_random_combination == 'randomize_rotate':
        given_image_left_and_right = apply_combination_of_functions_by_numpying_it(given_image_left_and_right, 'no_color', 'no_flip', 'any_rotate', 'no_making')
    elif given_random_combination == 'randomize_making':
        given_image_left_and_right = apply_combination_of_functions_by_numpying_it(given_image_left_and_right, 'no_color', 'no_flip', 'no_rotate', 'any_making')

    if given_random_combination == 'randomize_flip':
        given_image_center = apply_combination_of_functions_by_numpying_it(given_image_center, 'no_color', 'any_flip', 'no_rotate', 'no_making')
    elif given_random_combination == 'randomize_rotate':
        given_image_center = apply_combination_of_functions_by_numpying_it(given_image_center, 'no_color', 'no_flip', 'any_rotate', 'no_making')
    elif given_random_combination == 'randomize_making':
        given_image_center = apply_combination_of_functions_by_numpying_it(given_image_center, 'no_color', 'no_flip', 'no_rotate', 'any_making')

    
    given_image_blue = cbof.color_the_image(given_image_top,'to_blue')
    given_image_row_blue = np.hstack([given_image_blue] * hstack_factor_blue)

    given_image_green = cbof.color_the_image(given_image_bottom,'to_green')
    given_image_row_green = np.hstack([given_image_green] * hstack_factor_green)

    given_image_red = cbof.color_the_image(given_image_left_and_right,'to_red')
    given_image_column_red = np.vstack([given_image_red] * vstack_factor_red)

    given_image_double = cbof.make_the_image(given_image_center,'double_size')
    given_image_row_red_and_double = np.hstack((given_image_column_red, given_image_double))
    given_image_row_red_and_double_and_red_again = np.hstack((given_image_row_red_and_double, given_image_column_red))

    given_image_to_show = given_image_row_blue
    given_image_to_show = np.vstack((given_image_to_show, given_image_row_red_and_double_and_red_again))
    given_image_to_show = np.vstack((given_image_to_show, given_image_row_green))
   
    return given_image_to_show

# ----------------------------------------------------------------
# Functions <*>_by_plotting_it hereunder only to be used with the function, first subplotting solution
# create_colorful_big_one_by_plotting_it(given_image, instruction_list, save_image_path)
# ----------------------------------------------------------------
def create_colorful_big_one_by_plotting_it(given_image, instruction_list, save_image_path):

    """ This function will draw the colorful_big_one image
        by just using the subplot python fuctions
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
        cbof.save_the_image(save_image_path)
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
def create_instructed_image_by_plotting_it(given_image, instruction):

    """ 
    
    This function will apply the instruction given on a given image.  

    It can only be used together with the function
    create_colorful_big_one_by_plotting_it(given_image, instruction_list, save_image_path)
    where it is used the generate each sepeate image from the randomized instruciton list

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
    result as a vertical flip with a right rotation
        
    """
    
    given_image = cbof.color_the_image(given_image, instruction[0])
    given_image = cbof.flip_the_image(given_image, instruction[1])
    given_image = cbof.rotate_the_image(given_image, instruction[2])
    given_image = cbof.make_the_image(given_image, instruction[3])
    
    return given_image
  
# ----------------------------------------------------------------    
def generate_random_instruction_list_by_plotting_it():

    """ 
    
    This functon creates a list of 144 instructions and then randomizes it.

    It can only be used together with the function
    create_colorful_big_one_by_plotting_it(given_image, instruction_list, save_image_path)
    where it randomizes the parameter instruction list
        
    Please note an instruction is a list of 4 possible image processing options
    An instruction list is thus a list of lists
        
    please note the process option "double_size" is not used in the randomisation function
    
    """
    
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
