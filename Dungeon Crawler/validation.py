#accepts the (x,y) coordinates for the intended move or object placement
#checks to see if coordinates are within the limits of the array
#returns true if coordinates exceed the set bounds, returns false if the coordinates fall within the acceptable range
def out_of_bounds (x_axis, y_axis, bounds, movement):
    #moveTarget(x_axis, y_axis, movement)
    if (x_axis >= bounds or x_axis < 0 or y_axis >= bounds or y_axis < 0):
        return true
    return false

#accepts layout of the current floor of the dungeon, and the proposed x and y coordinates as well as the object being looked for
#tests to see if proposed placement is within one square of designated test object
#returns true if object is within one space, returns false if object is not within one space
def too_close (dungeon, current_floor, bounds, x_axis, y_axis, target_object):
    if (out_of_bounds(x_axis, y_axis, bounds, NORTH) == False and checkMove(dungeon, current_floor, x_axis, y_axis, NORTH, target_object) == True):
        return true
    if (out_of_bounds(x_axis, y_axis, bounds, WEST) == False and checkMove(dungeon, current_floor, x_axis, y_axis, WEST, target_object) == True):
        return true
    if (out_of_bounds(x_axis, y_axis, bounds, SOUTH) == False and checkMove(dungeon, current_floor, x_axis, y_axis, SOUTH, target_object) == True):
        return true
    if (out_of_bounds(x_axis, y_axis, bounds, EAST) == False and checkMove(dungeon, current_floor, x_axis, y_axis, EAST, target_object) == True):
        return true
    return false


# Validation of integer input within a designated range.
# Accepts maximum and minimum input to constrain the range of valid choices.
# protects the cin stream from bad input and continues to ask the user for input until user chooses input within the acceptable range limitations
# Returns valid integer value.
def int_input(MIN_INPUT, MAX_INPUT):
    invalid = True
    while invalid:
        try:
            userInput = int(input())
        except ValueError:
            print("Attempted input is not an integer value, please try again")
            continue
        if (userInput < MIN_INPUT or userInput > MAX_INPUT):
            print("Your input is not within acceptable parameters for this program.")
            print("Please enter a number within the given range of " + str(MIN_INPUT) + " to " + str(MAX_INPUT) + "\n")
        else:
            invalid = False
    return userInput

# Obtains valid input for yes/no questions.
# Accepts no arguments.
# Returns true if yes, false if no.
def yes_or_no():
    print("Please select Y for yes or N for no.")
    validInput = input() # obtains initial input value
    while (validInput != 'y' and validInput != 'Y' and validInput != 'n' and validInput !='N'): #tests input value against all acceptable inputs, enters loop if value is not within accepted parameters
        print("Invalid input, please select Y or N")
        validInput = input();
    if (validInput == 'y' or validInput == 'Y'):
        return True
    else:
        return False
    


