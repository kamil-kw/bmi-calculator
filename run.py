"""
scope:
- Welcome message
- Type your name
- Hi <name> 
-- BMI tool
- Give your input
    - Gender
    - Age
    - Height
    - Weight
- calulate
- Print result
- do it again?
"""
def is_digit(user_input):
    """
    Function is checking if value is number
    return true or false
    """
    if any(char.isdigit() for char in user_input):
        return True
    else:
        return False

def user_input_name():
    """
    Function colecting a user name and use it globally
    and checking vaule if string usnig is_digit()
    """
    global name
    name = input('Please enter your name:\n')
    if is_digit(name) is True:
        print("Please do not include digits in your name.")
        user_input_name()
    else:
        return name


def user_input_age():
    """
    Function colecting a user age 
    and checking vaule if is digit using is_digit()
    """
    age = input(f"Hi {name.capitalize()} please enter your age:\n")
    if is_digit(age) is False:
        print("Please do not include letter in your age.")
        user_input_age()
    elif int(age) > 120:
        print("Is this a correct age?")
        user_input_age()
    else:
        return age

def choose_unit():
    """
    Function will collect information about unit of measurment standard
    """
    enter = 'Enter unit of measurement by typing a number:\n'
    si = '1. The International System of Units (SI)\n'
    usc = '2. United States Customary Units (USC)\n'
    global enter_weight
    unit_type = input(f"{enter}\n{si}\n{usc}\n")
    if unit_type == "1":
        print(f"{name.capitalize()} the units you choosed is SI")
        enter_weight = "please enter your weight in kg"
        return True
    elif unit_type == "2":
        print(f"{name.capitalize()} the units you choosed is USC")
        enter_weight = "please enter your weight in lbs"
        return False
    else:
        print("Please choose correct value 1 or 2")
        choose_unit()


def user_input_weight():
    """
    Function colecting a user weight
    and checking vaule if is digit using is_digit()
    """
    weight = input(f"Hi {name.capitalize()} {enter_weight}:\n")

    if is_digit(weight) is False:
        print("Please do not include letter in your weight.")
        user_input_weight()
    else:
        return weight




def main():
    """
    Run all program functions
    """
    user_input_name()
    user_input_age()
    choose_unit()
    user_input_weight()




print("Welcome in the BMI Calculator")
main()