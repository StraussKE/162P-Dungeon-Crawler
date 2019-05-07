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
    


