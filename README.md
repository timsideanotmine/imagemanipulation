# imagemanipulation
Image manipulation in Numpy (Syntra) : Created by Johan Van Erum, monday 12th of February 2024

This coding to be evaluated by Tim Horemans, so he can quote the code for this part of the course.
Please have a look at the /documentation/assignment.md file (or assignment.pdf) to check on what exactly was asked 

## How to set up the enviroment 'IMAGEMANIPULATION'

Open a conda powershell prompt, activate the base enviroment if necessary 
Execute 'conda env create -f environment.yaml'
You can find the yaml file at \IMAGEMANIPULATION\environmment.yaml
Then activate the enviroment 'conda activate imagemanipulation'
Resulting in '(imagemanipulation) PS C:\imagemanipulation>'

## After setting up the environment, run the code

(imagemanipulation) PS C:\imagemanipulation>'python main.py' 

This will run the code and will present 4 solutions:
1. the first image requested in the test: 
an image replication 8 x 3 (tiled solution)

2. the second image requested in the test: 
an image replictaion 6 x 4 with each rown flipping/rotating the image differently

3. the 3rd image requested in the test:
an image replication 4 x 4 with a doubled size image in the center

4. Extra : 4th image
same image as 3. but each picture randomized in color, flip, rotation, process
colors uses : <original>
flip : flipping horizontally or vertically
rotate : rotate left or right
process : swirled, tirled, rippled (other available)

## Variants on how to execute

## running from another module, also used to import in main.py or in the notebooks

the code can also be executed from a conda power shell as follows:
(imagemanipulation) PS C:\imagemanipulation\scripts>'python colorful_big_one_solutions.py' 
This will activate the main() routine and will load a different image for the 4 described results here above

Note : the module 'colorful_big_one_functions.py' does not have a main() and contains the functions for
coloring, flipping, rotating and processing the image.
have a look at the module 'colorful_big_one_functions.py'
to see what functionality is available or use the 4th and 5th cel in 'imageprocessing_by_numpying_it.ipynb'
to test those functions

the code can also be executed from the notebook 'imageprocessing_by_numpying_it.ipynb'
by exceuting 'Run all' in VS code or
by executing is cell by cell

## other solutions, by using subplotting

## running from another module
this particular code can be executed from a conda power shell as follows:
(imagemanipulation) PS C:\imagemanipulation\scripts>'python colorful_big_one_old_solution_by_plotting_it.py' 
This will activate the main() routine and will load a subplotted image using a randomisation process
plotting 144 different variants of the same image, ussing the functions defined in 'colorful_big_one_functions.py'

