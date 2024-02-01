def main():

    default_image = 'kittycat_blebleble.png'
    # default_image = 'kittycat_waaah.png'
    # default_image = 'elon_star_wars.png'
    # default_image = 'no_testing_just_debugging.png'
    # default_image = 'wait_let_me_check_my_messages.png'
    # default_image = 'Awake_but_at_what_cost.png'
    
    default_image_path = os.path.join('..','images','input',default_image)

    loaded_image_path = default_image_path
    use_this_image = np.array(Image.open(loaded_image_path))

    #random_instructions_list = generate_random_instruction_list()
    create_colorful_big_one(use_this_image, generate_random_instruction_list())

    return

# ----------------------------------------------------------------
def color_image(given_image, color):

    """ This function will turn an image into the given color """
    
    if color == "red_color":
        given_image[:,:,[1,2]] = 0
        return given_image
    
    elif color == "blue_color":
        given_image[:,:,[0,1]] = 0
        return given_image
    
    elif color == "green_color":
        given_image[:,:,[0,2]] = 0
        return given_image
    
    else:
        # "no_color or faulty color"
        return given_image

# ----------------------------------------------------------------    
def flip_image(given_image, manner_of_flip):

    """ This function will flip an image horizontally or vertically according to the given manner_of_flip """

    if manner_of_flip == "horizontal_flip":
        given_image = np.fliplr(given_image)
        return given_image
    
    elif manner_of_flip == "vertical_flip":
        given_image = flip_image(given_image, "horizontal_flip")
        given_image = rotate_image(given_image, "left_rotation")
        given_image = rotate_image(given_image, "left_rotation")
        return given_image

    else:
        # "no_flip or faulty manner_of_flip"
        return given_image
    
# ----------------------------------------------------------------
def rotate_image(given_image, manner_of_rotation):

    """ This function will rotate an image according to the manner_of_rotation """

    if manner_of_rotation == "left_rotation":
        given_image = np.rot90(given_image)
        return given_image
    
    elif manner_of_rotation == "right_rotation":
        given_image = np.rot90(given_image, 3)
        return given_image

    else:
        # "no_rotation or faulty rotation"
        return given_image
    
# ----------------------------------------------------------------
def apply_to_image(given_image, process):

    """ This function will make an image according to the process requested """
    
    if process == "noise_making":
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
    
    elif process == "black_and_white_making":    
        given_image = given_image.astype(float)
        given_image = given_image.sum(axis = 2)
        given_image /= given_image.max()
        given_image = np.absolute(given_image)
        return given_image
    
    elif process == "shady_making":        
        given_image = np.where(given_image > 150, 150 , 20)
        return given_image
    
    else:
        # "no_making or faulty making"
        return given_image    
        
# ----------------------------------------------------------------
def create_colorful_big_one(given_image, instruction_list):

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
            part_of_colorful_big_one = create_instructed_image(part_of_colorful_big_one, instruction_list[grid_position-1])
            if instruction_list[grid_position-1][3] == "black_and_white_making":
                plt.imshow(part_of_colorful_big_one, cmap=plt.cm.gray)    
            else:
                plt.imshow(part_of_colorful_big_one)

            # reporting as to how far the process has evolved    
            print(f"** step 3 ** Instruction for grid position {grid_position} was processed", end='\r')
                        
    print()
    print(f"** step 3 ** Original image with red colored title is on row {row_original_image}, column {column_original_image}, grid postion {grid_position_original_image}")
    print()

    # saving the image with datetime stamp
    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.strftime("%Y%m%d_%H%M%S")
    filename = f"colorful_big_one_{timestamp}.png"
    save_image_path = os.path.join('..', 'images','output', filename)
    print(f"** step 4 ** Saving the resulting colorful_big_one image as {save_image_path} \n")
    plt.savefig(save_image_path, format="png")

    # showing the result on screen
    print(f"** step 5 ** Executing the plt.show() instruction .. yep, still busy ...  \n")
    #plt.title(use_this_image)
    #plt.title(main().use_this_image)
    plt.show()
    plt.close
   
    print(f"** step 6 ** All done, do you like the result ? \n")
    
# ----------------------------------------------------------------  
def create_instructed_image(given_image, instruction):

    """ This function will apply the instruction given on a given image.  

        A single instruction is composed of 4 possible image processing options
        in the predefined order as given hereunder :
        
        [color, manner_of_flip, manner_of_rotation, process]
        
        color : set color of image to red, green, blue or no color
        manner_of_flip = do a horizontal or vertical flip or do no flip with the image
        manner_of_rotation = do a left or right rotation or do no rotation with the image
        process = apply the process of making the image noisy, shady, black and white or do nothing
        
        please note the process of making an image black and white is not regarded 
        as setting a color, but rather as removing the color from an image. That means
        an image can be colorized first but end up being made black_and_whtite
        
        please also note that a horizontal flip and a left rotation produces the same
        result as a vertical flip with a right rotation"""
    
    given_image = color_image(given_image, instruction[0])
    given_image = flip_image(given_image, instruction[1])
    given_image = rotate_image(given_image, instruction[2])
    given_image = apply_to_image(given_image, instruction[3])
    
    return given_image
  
# ----------------------------------------------------------------    
def generate_random_instruction_list():

    """ This functon creates a list of 144 instructions and then randomizes it.
        
        Please note an instruction is a list of 4 possible image processing options
        An instruction list is thus a list of lists"""
    
    colors = ["no_color", "red_color", "green_color", "blue_color"]
    flips = ["no_flip", "horizontal_flip", "vertical_flip"]
    rotations = ["no_rotation", "left_rotation", "right_rotation"]
    makings = ["no_making", "noise_making", "black_and_white_making", "shady_making"]

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

    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image
    import os 
    import datetime

    main()
