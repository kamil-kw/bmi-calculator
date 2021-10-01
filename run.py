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


def collect_name(user_name):
    """
    Check user name input and return result
    """
    if any(char.isdigit() for char in user_name):
        print("Please do not include digits in your name.")
        main()
    else:
        print("Nice to meet you " + user_name)
        return user_name


def collect_age(user_age):
    """
    Check user age input and return result
    """
    if any(char.isalpha() for char in user_age):
        print("Please do not include letters in your age.")
    else:
        print("Your age is " + user_age)
        return user_age


def main():
    """
    Run all program functions
    """
    name = input('Please enter your name:\n')
    user_name = str(name)
    collect_name(user_name)
    age = input('Please enter your age:\n')
    user_age = age
    collect_age(user_age)


print("Welcome in the BMI Calculator")
main()
