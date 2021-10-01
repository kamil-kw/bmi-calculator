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
    else:
        return age

def choose_unit():
    enter = 'Enter unit of measurement by typing a number:\n'
    si = '1. The International System of Units (SI)\n'
    usc = '2. United States Customary Units (USC)\n'
    unit = input(f"{enter}\n{si}\n{usc}\n")
    if unit == "1":
        print(f"{name.capitalize()} the units you choosed in SI")
        return True
    elif unit == "2":
        print(f"{name.capitalize()} the units you choosed in USC")
        return False
    else:
        print("Please choose correct value 1 or 2")
        choose_unit()

def main():
    """
    Run all program functions
    """
    user_input_name()
    user_input_age()
    choose_unit()




print("Welcome in the BMI Calculator")
main()