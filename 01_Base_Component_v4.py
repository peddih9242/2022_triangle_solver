# import modules

import math
import pandas

# functions

# string checker, checks for valid input from mini lists
def string_checker(question, valid_list, error, help_response):
    
    # loop taking in input and string checking process
    valid = False
    while not valid:
        
        # take input
        response = input(question).lower()
        
        # if the user asks for help then give help based on question
        if response == "help":
            print(help_response)

        else:
            # compare response with items in list
            for var_list in valid_list:
                if response in var_list:
                    response = var_list[0]
                    var_valid = True
                    break
                else:
                    var_valid = False
        
            # if response is found to be valid, return first item in valid list otherwise print error
            if var_valid == True:
                return response
            else:
                print(error)
                print()


# number checker, checks for float above 0 and below high if given
def num_check(question, error, high=None):

    have_high = False

    if high:
        have_high = True

    valid = False
    while not valid:
        try:
            # ask user for number
            response = float(input(question))
            
            # check that number is above 0 and lower than high if given
            if response <= 0:
                print(error)
                continue

            if have_high:
                if response >= high:
                    print(error)
                    continue

            return response

        # if input is not a number print an error
        except ValueError:
            print(error)
            print()


# formats trailing 0s off floats
def trail_formatting(var_number):
    var_number = round(var_number, 2)
    return "%g"%(var_number)

# blank checking function, checks if a string input is blank
def not_blank(question, error):
    
    var_loop = True
    while var_loop:
    
    # take in response and check if it is blank
        response = input(question).lower()
        
        if response != "":
            return response
        else:
            print(error)

# returns given item with units
def unit_format(format_num, unit):
    return "{} {}".format(format_num, unit)

# asks if user needs instructions and prints instructions if needed
def instructions():
    instruction_help = "If you haven't used this program before, read the instructions."
    print_instructions = string_checker("Do you want to see the instructions? ", yes_no, "Please enter yes or no.", instruction_help)

    if print_instructions == "yes":
        print()
        print("**** Welcome to the Triangle Solver! ****")
        print("- In this program, you will be asked questions about your triangle.")
        print("- Answer those questions and this program will calculate the part of your triangle that you're looking for!")
        print("- It is important to note that if you don't understand a word question, you can type 'help' which will explain the question in a way that you can *hopefully* understand.")
        print("- You can do as many calculations as you want, and when you stop the stats for each calculation will be written to a .txt file under the name 'triangle_stats.txt'.")
    return ""

# calculates whole triangle when given two sides or a side and an angle
def triangle_solver():

    # get units for triangle lengths
    unit_help = "You should input the units that your lengths have (e.g. centimetres/cm), if you don't have units press <enter> to skip to the next question."
    triangle_unit = string_checker("What units are your length(s) in? ", valid_units, "Please enter a valid unit!", unit_help)

    # ask user questions to find if user has two sides or a side and an angle
    # making sure that first side is not blank and both sides are not the same
    while True:
        what_side_help = "\nWe need to know if your side is the hypotenuse / opposite / adjacent. \n- If your side is the longest side, it's the hypotenuse. \n- If your angle is right next to the side you have, it's the adjacent. \n- If your side is on the other side of the angle, it's the opposite.\n- If you only have one side, the second time you're asked for your side press <enter> to skip the question.\n"
        what_side_1 = string_checker("What side do you have? ", side_valid, "Please enter a valid side.", what_side_help)
        
        if what_side_1 == "":
            print("Please don't enter blank!")
            continue
    
        what_side_2 = string_checker("What side do you have? ", side_valid, "Please enter a valid side.", what_side_help)
        
        if what_side_1 != what_side_2:
            break
        print("Please don't enter the same sides!")

    side_1 = num_check("How long is your {}? ".format(what_side_1), "Please enter a number above 0.")
    
    # differentiate between 2 sides and side + angle then calculate the whole triangle
    if what_side_2 == "":
        
        # start of path where user has side and angle
        angle_1 = num_check("How large is your angle? ", "Please enter a number above 0 and below 90.", 90)
        
        # calculate other angle using geometric reasoning - all angles in triangle add to 180
        angle_2 = 90 - angle_1
        
        # use trigonometry to calculate the hypotenuse or another side if already given then use pythagoras to calculate the last side
        if what_side_1 == "hypotenuse":
            side_2 = side_1 * math.sin(math.radians(angle_1))
            side_3 = ((side_1 ** 2) - (side_2 ** 2)) ** 0.5
        else:
            if what_side_1 == "opposite":
                side_2 = side_1 / math.sin(math.radians(angle_1))
            
            elif what_side_1 == "adjacent":
                side_2 = side_1 / math.cos(math.radians(angle_1))
            side_3 = ((side_2 ** 2) - (side_1 ** 2)) ** 0.5

    else:

        # start of user having 2 sides
        # make sure that hypotenuse is the longest side if hypotenuse has been given by user
        while True:
            side_2 = num_check("How long is your {}? ".format(what_side_2), "Please enter a number above 0.")
            if what_side_1 == "hypotenuse" and side_2 >= side_1 or what_side_2 == "hypotenuse" and side_1 >= side_2:
                print("Please make sure your hypotenuse is the longest side!")
            
            else:
                break 

        # use pythagoras to calculate the third side
        if what_side_1 == "hypotenuse":
            side_3 = ((side_1 ** 2) - (side_2 ** 2)) ** 0.5
        elif what_side_2 == "hypotenuse":
            side_3 = ((side_2 ** 2) - (side_1 ** 2)) ** 0.5
        else:
            side_3 = ((side_1 ** 2) + (side_2 ** 2)) ** 0.5

        # use SOH CAH TOA to calculate one angle
        if what_side_1 == "hypotenuse":
        
            if what_side_2 == "opposite":
                angle_1 = math.asin(side_2 / side_1)
        
            elif what_side_2 == "adjacent":
                angle_1 = math.acos(side_2 / side_1)
        
        elif what_side_2 == "hypotenuse":
            
            if what_side_1 == "opposite":
                angle_1 = math.asin(side_1 / side_2)
        
            elif what_side_1 == "adjacent":
                angle_1 = math.acos(side_1 / side_2)
        
        else:

            if what_side_1 == "opposite":
                angle_1 = math.asin(side_1 / side_3)
            
            elif what_side_1 == "adjacent":
                angle_1 = math.acos(side_1 / side_3)
        
        # convert angle from radians to degrees and calculate last angle
        angle_1 = math.degrees(angle_1)
        angle_2 = 90 - angle_1
    

    # formatting sides and angles then append to lists and printing
    side_1 = unit_format(trail_formatting(side_1), triangle_unit)
    side_2 = unit_format(trail_formatting(side_2), triangle_unit)
    side_3 = unit_format(trail_formatting(side_3), triangle_unit)
    angle_1 = unit_format(trail_formatting(angle_1), "°")
    angle_2 = unit_format(trail_formatting(angle_2), "°")

    lengths_1.append(side_1)
    lengths_2.append(side_2)
    lengths_3.append(side_3)
    first_angles.append(angle_1)
    second_angles.append(angle_2)
    
    print("Side 1:", side_1)
    print("Side 2:", side_2)
    print("Side 3:", side_3)
    print("Angle 1:", angle_1)
    print("Angle 2:", angle_2)

    return ""

# main routine

# string checking lists

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

side_angle = [
    ["length", "side length", "width", "side", "l"],
    ["angle", "angle size", "a"]
]

trig_valid = [
    ["sin", "s"],
    ["cos", "c"],
    ["tan", "t"]
]

side_valid = [
    ["hypotenuse", "hyp", "h"],
    ["opposite", "opp", "o"],
    ["adjacent", "adj", "a"]
]

valid_units = [
    ["cm", "centimetres", "centimetre", "centimeters", "centimeter"],
    ["km", "kilometres", "kilometre", "kilometers", "kilometer"],
    ["mm", "millimetres", "millimetre", "millimeters", "millimeter"],
    ["m", "metres", "metre", "meters", "meter"],
    ["mi", "miles", "mile"],
    ["in", "inches", "inch"],
    ["megametres", "megameter", "megametre", "megameters"],
    ["yds", "yards", "yd", "yard"],
    ["ft", "foot", "feet"],
    ["", "no unit", "none", "n", "unit", "units"]
]

trig_pyth_valid = [
    ["trigonometry", "trig", "t"],
    ["pythagoras", "pythagoras theorem", "pythag", "p"]
]

calc_count = []
lengths_1 = []
lengths_2 = []
lengths_3 = []
first_angles = []
second_angles = []

# set up dictionary for results
results_dict = {
    "Calculation": calc_count,
    "Length 1": lengths_1,
    "Length 2": lengths_2,
    "Length 3": lengths_3,
    "Angle 1": first_angles,
    "Angle 2": second_angles,
}

instructions()

round_count = 0
keep_going = "yes"
while keep_going == "yes":
    
    print()
    round_count += 1
    calc_count.append(round_count)
    # ask questions and get triangle answer
    triangle_solver()
    
    keep_going_help = "If you want to keep going, enter yes, otherwise enter no to exit."
    keep_going = string_checker("Do you want to do another calculation? ", yes_no, "Please enter yes or no.", keep_going_help)

print("\n\n")
print("**** Triangle Solver Stats ****")
print()
results_frame = pandas.DataFrame(results_dict, columns = ['Calculation', 'Length 1', 'Length 2', 'Length 3', 'Angle 1', 'Angle 2'])
results_frame = results_frame.set_index('Calculation')
print(results_frame)

# change dataframe to text for writing to file
results_txt = pandas.DataFrame.to_string(results_frame)

# set up write to file
file_name = "triangle_stats.txt"
text_file = open(file_name, "w+")

# heading
text_file.write("**** Triangle Solver Stats ****")
text_file.write("\n\n")
text_file.write(results_txt)
text_file.close()