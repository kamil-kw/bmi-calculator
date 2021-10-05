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
    # if characters is digit return boolean
    if any(char.isdigit() for char in user_input):
        return True
    else:
        return False


def is_letter(user_input):
    """
    Function is checking if value is number
    return true or false
    """
    # if characters is digit return boolean
    if any(char.isalpha() for char in user_input):
        return True
    else:
        return False


def user_input_name():
    """
    Function colecting a user name and use it globally
    and checking value if is string using is_digit() function
    """
    # variable to use outcome globally in other functions
    global name
    # User name input
    name = input('Please enter your name:\n')
    # if characters is digit message and repeat function
    if is_digit(name) is True:
        print("Please do not include digits in your name.")
        user_input_name()
    # else return name
    else:
        return name


def user_input_age():
    """
    Function colecting a user age and checks if value is
    digit using is_digit() function
    """
    # variable to use outcome globally in other functions
    global age
    # User age input
    age = input(f"Hi {name.capitalize()} please enter your age:\n")
    # if characters is letter message and repeat function
    if is_letter(age) is True:
        print("Please do not include letter in your age.")
        user_input_age()
    elif int(age) >= 120:
        print("Is this a correct age?")
        user_input_age()
    else:
        return age


def choose_unit():
    """
    Function will collect information about unit of measurment standard
    """
    # variable to ensure PEP8 convention pass (amount of characters in line)
    enter = 'Enter unit of measurement by typing a number:\n'
    si = '1. The International System of Units (SI) cm or kg\n'
    usc = '2. United States Customary Units (USC) in or lbs\n'
    # variables to use outcome globally in other functions
    global enter_weight
    global enter_height
    global unit_type
    unit_type = input(f"{enter}\n{si}\n{usc}\n")
    if unit_type == "1":
        print(f"{name.capitalize()} the units you choosed is SI\n")
        enter_weight = "please enter your weight in kg"
        enter_height = "please enter your height in cm"
    elif unit_type == "2":
        print(f"{name.capitalize()} the units you choosed is USC\n")
        enter_weight = "please enter your weight in lbs"
        enter_height = "please enter your height in in"
    else:
        print("Please choose correct value 1 or 2\n")
        choose_unit()


def user_input_weight():
    """
    Function colecting a user weight
    and checking vaule if is digit using is_digit()
    """
    # variable to use outcome globally in other functions
    global weight
    weight = input(f"Hi {name.capitalize()} {enter_weight}:\n")

    if is_digit(weight) is False:
        print("Please do not include letter in your weight.\n")
        user_input_weight()
    else:
        return weight


def user_input_height():
    """
    Function colecting a user height
    and checking value if is digit using is_digit() function
    """
    # variable to use outcome globally in other functions
    global height
    height = input(f"Hi {name.capitalize()} {enter_height}:\n")

    if is_digit(height) is False:
        print("Please do not include letter in your height.\n")
        user_input_height()
    else:
        return height


def bmi_calculator():
    global bmi
    if unit_type == "1":
        bmi = round(float(weight)/(float(height)/100)**2, 2)
        print(f"{name.capitalize()} your BMI is {bmi} kg/m^2\n")
    else:
        bmi = round(float(weight)/(float(height)**2)*703, 2)
        print(f"{name.capitalize()} your BMI is {bmi} lbs/in^2\n")


def bmi_categories():
    """
    Function will describe bmi score based on age
    """
    # variable to ensure PEP8 convention pass (amount of characters in line)
    your_bmi = "your BMI Category is "
    if int(age) < 18:
        """
        If age of user is below 18
        """
        if float(bmi) <= 18.5:
            print(f"{name.capitalize()} {your_bmi}underweight\n")
        elif float(bmi) >= 18.5 and float(bmi) <= 24.9:
            print(f"{name.capitalize()} {your_bmi}normal\n")
        elif float(bmi) >= 25 and float(bmi) <= 29.9:
            print(f"{name.capitalize()} {your_bmi}overweight\n")
        else:
            print(f"{name.capitalize()} {your_bmi}obesity\n")
    else:
        """
        If age of user is over 18 - adults
        """
        if float(bmi) <= 16:
            print(f"{name.capitalize()} {your_bmi}Severe Thinness\n")
        elif float(bmi) >= 16 and float(bmi) <= 17:
            print(f"{name.capitalize()} {your_bmi}Moderate Thinness\n")
        elif float(bmi) >= 17 and float(bmi) <= 18.5:
            print(f"{name.capitalize()} {your_bmi}Mild Thinness\n")
        elif float(bmi) >= 18.5 and float(bmi) <= 25:
            print(f"{name.capitalize()} {your_bmi}Normal\n")
        elif float(bmi) >= 25 and float(bmi) <= 30:
            print(f"{name.capitalize()} {your_bmi}Overweight\n")
        elif float(bmi) >= 30 and float(bmi) <= 35:
            print(f"{name.capitalize()} {your_bmi}Obese Class I\n")
        elif float(bmi) >= 35 and float(bmi) <= 40:
            print(f"{name.capitalize()} {your_bmi}Obese Class II\n")
        else:
            print(f"{name.capitalize()} {your_bmi}Obese Class III\n")


def restart_calculator():
    """
    This function will recive user input y - continue or n - exit
    """
    # variables to ensure PEP8 convention pass (amount of characters in line)
    repeat = "Do you want to repeat calculations?"
    yes = "Press 'y' than 'enter' to continue calculations"
    no = "Press 'n' than 'enter' to quit calculations"
    restart = input(f"{repeat}\n{yes}\n{no}\n")
    if restart == 'y':
        print('Calculate again')
        main()
    elif restart == 'n':
        exit()
    else:
        print("Incorrect character, please type 'y' or 'n'\n")
        restart_calculator()


def main():
    """
    Run all program functions
    """
    user_input_name()
    user_input_age()
    choose_unit()
    user_input_weight()
    user_input_height()
    bmi_calculator()
    bmi_categories()
    restart_calculator()


print("Welcome in the BMI Calculator\n")
main()