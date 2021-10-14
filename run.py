def is_digit(user_input):
    """
    Function is checking if value is a number
    return boolean True or False
    """
    # if any characters is digit return boolean True else False
    if any(char.isdigit() for char in user_input):
        return True
    return False


def is_letter(user_input):
    """
    Function is checking if value is a letter
    return boolean True or False
    """
    # if any characters is letter -> return boolean True else False
    if any(char.isalpha() for char in user_input):
        return True
    return False


def user_input_name():
    """
    Function collecting a user name and use it globally
    and checking value if is string using is_digit() function
    """
    # variable to use outcome globally in other functions
    global name
    # User name input
    name = input('\n\033[1;32;10mPlease enter your name:\n')
    # if characters is digit -> message to user and repeat this function
    if is_digit(name) is True:
        print("\033[1;31;10mPlease do not include digits in your name.")
        user_input_name()
    # else return name
    return name


def user_input_age():
    """
    Function collecting a user age and checks if value is
    digit using is_digit() function
    """
    # variable to use outcome globally in other functions
    global age
    # variable to ensure PEP8 convention pass (amount of characters in line)
    enter_age = " please enter your age:"
    # User age input
    age = input(f"\n\033[1;32;10mHi {name.capitalize()}{enter_age}\n")
    # if characters is letter -> message to user and repeat this function
    if is_letter(age) is True:
        print("\n\033[1;31;10mPlease do not include letter in your age.")
        user_input_age()
    # if age is to high over 120 -> message to user and repeat this function
    elif int(age) >= 120:
        print("\n\033[1;31;10mIs this a correct age?")
        user_input_age()
    # else return age
    return age


def choose_unit():
    """
    Function will collect information about user preferences
    about unit of measurement
    """
    # variable to ensure PEP8 convention pass (amount of characters in line)
    enter = 'Enter unit of measurement by typing a number:\n'
    si = '1. The International System of Units (SI) cm or kg'
    usc = '2. United States Customary Units (USC) in or lbs\n'
    # variables to use outcome globally in other functions
    global enter_weight
    global enter_height
    global unit_type
    # User measurement unit input
    unit_type = input(f"\n\033[1;32;10m{enter}\n{si}\n{usc}\n")
    # if user typed 1 -> message about choice - and return comment
    if unit_type == "1":
        print(f"\n{name.capitalize()} the units you have choosen is SI\n")
        enter_weight = "please enter your weight in kg"
        enter_height = "please enter your height in cm"
    # if user typed 2 -> message about choice - and return comment
    elif unit_type == "2":
        print(f"\n{name.capitalize()} the units you have choosen is USC\n")
        enter_weight = "please enter your weight in lbs"
        enter_height = "please enter your height in in"
    # if user typed other value -> message about choice - and repeat function
    else:
        print("\033[1;31;10mPlease choose correct value 1 or 2\n")
        choose_unit()


def user_input_weight():
    """
    Function collecting a user weight
    and checking value if is digit using is_digit()
    """
    # variable to use outcome globally in other functions
    global weight
    # User weight input
    weight = input(f"\n\033[1;32;10mHi {name.capitalize()} {enter_weight}:\n")
    # if characters is digit -> message to user and repeat this function
    if is_letter(weight) is True:
        print("\n\033[1;31;10mPlease do not include letter in your weight.")
        user_input_weight()
    # else return weight
    return weight


def user_input_height():
    """
    Function collecting a user height
    and checking value if is digit using is_digit() function
    """
    # Variable to use outcome globally in other functions
    global height
    # User height input
    height = input(f"\n\033[1;32;10mHi {name.capitalize()} {enter_height}:\n")
    # If characters is digit -> message to user and repeat this function
    if is_letter(height) is True:
        print("\n\033[1;31;10mPlease do not include letter in your height.")
        user_input_height()
    # Else return weight
    return height


def bmi_calculator():
    # Variable to use outcome globally in other functions
    global bmi
    # Calculation if unit type SI, float to allow 2 digits after comma
    if unit_type == "1":
        bmi = round(float(weight)/(float(height)/100)**2, 2)
        print(f"\n{name.capitalize()} your BMI is {bmi}")
    # Calculation if unit type USC, float to allow 2 digits after comma
    else:
        bmi = round(float(weight)/(float(height)**2)*703, 2)
        print(f"\n{name.capitalize()} your BMI is {bmi}")


def bmi_categories():
    """
    Function will describe bmi score based on age
    """
    # variable to ensure PEP8 convention pass (amount of characters in line)
    your_bmi = "your BMI Category is "
    # result to user in age below 18
    if int(age) < 18:
        """
        If age of user is below 18
        """
        if float(bmi) <= 18.5:
            print(f"{name.capitalize()} {your_bmi}underweight")
        elif float(bmi) >= 18.5 and float(bmi) <= 24.9:
            print(f"{name.capitalize()} {your_bmi}normal")
        elif float(bmi) >= 25 and float(bmi) <= 29.9:
            print(f"{name.capitalize()} {your_bmi}overweight")
        else:
            print(f"{name.capitalize()} {your_bmi}obesity")
    # Else result to user in age is over 18
    else:
        """
        If age of user is equal or over 18 - adults
        """
        if float(bmi) <= 16:
            print(f"{name.capitalize()} {your_bmi}Severe Thinness")
        elif float(bmi) >= 16 and float(bmi) <= 17:
            print(f"{name.capitalize()} {your_bmi}Moderate Thinness")
        elif float(bmi) >= 17 and float(bmi) <= 18.5:
            print(f"{name.capitalize()} {your_bmi}Mild Thinness")
        elif float(bmi) >= 18.5 and float(bmi) <= 25:
            print(f"{name.capitalize()} {your_bmi}Normal")
        elif float(bmi) >= 25 and float(bmi) <= 30:
            print(f"{name.capitalize()} {your_bmi}Overweight")
        elif float(bmi) >= 30 and float(bmi) <= 35:
            print(f"{name.capitalize()} {your_bmi}Obese Class I")
        elif float(bmi) >= 35 and float(bmi) <= 40:
            print(f"{name.capitalize()} {your_bmi}Obese Class II")
        else:
            print(f"{name.capitalize()} {your_bmi}Obese Class III")


def restart_calculator():
    """
    This function will receive user input y - continue or n - exit
    """
    # variables to ensure PEP8 convention pass (amount of characters in line)
    repeat = "Do you want to repeat calculations?"
    yes = "Press 'y' than 'enter' to continue calculations"
    no = "Press 'n' than 'enter' to quit calculations"
    # User decision y or n input
    restart = input(f"\033[1;32;10m\n{repeat}\n{yes}\n{no}\n")
    if restart == 'y':
        print('\n\033[1;33;10mCalculate again\n')
        main()
    elif restart == 'n':
        print('\n\033[1;33;10mSee you next time')
        exit()
    else:
        print("\n\033[1;31;10mIncorrect character, please type 'y' or 'n'")
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


print("\n\033[1;34;10mWelcome in the BMI Calculator\n")
print("\033[1;31;10m*******************************************\n")
print("\033[1;31;10m  #       #####    ##    ##   ##        #")
print("\033[1;32;10m #        ##  ##   ###  ###   ##         #")
print("\033[1;34;10m#         ######   ## ## ##   ##          #")
print("\033[1;35;10m #        ##  ##   ##    ##   ##         #")
print("\033[1;33;10m  #       #####    ##    ##   ##        #\n")
print("*******************************************")
print("\n\033[1;34;10mBody Mass Index for Everyone")
print("\n\033[1;35;10mUse this calculator to check your body mass index (BMI)")
print("Type your age and body details weight & height than program will")
print("calculate your BMI index based on details provided")


main()
