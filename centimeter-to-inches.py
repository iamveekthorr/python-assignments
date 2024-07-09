import re 
import math

'''This function will take in an integer as 
the value in centimeters (cm) and return an integer'''

def convert_cm_to_inches(cm: float ) -> float:
    try:
        return math.floor(float(cm / 2.54))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

#  This function is responsible for calculating the weight
def centimeters_to_inches():
    try:
        # Get the weigh from the user
        untrusted_input = input("Please enter your centimeter value: ")
        inch = 0
        
        # Regular expression to check for alphabets 
        starts_with_alphabets = re.compile('^[A-Za-z]+$')
        starts_with_alphabets_but_contains_numbers = re.compile('^[A-Za-z].*\d')
        
        # This will check if the user has only entered alphabets
        if (re.match(starts_with_alphabets, untrusted_input) 
           or re.match(starts_with_alphabets_but_contains_numbers, untrusted_input)):
            raise ValueError("Invalid input!. Input must start with a number.")
        
        # first check if the user entered the unit (cm)
        # the strip() function will remove whitespaces anywhere in the input
        if (untrusted_input.__contains__('cm')):
            centimeter_value = untrusted_input.strip().split('cm')
            inch = math.floor(float(centimeter_value[0])) 
            # Check if given value is a positive number greater than 1
            if (inch < 0):
                raise ValueError("Invalid input!. Value cannot be negative or less than or equal to 1.")
            
            print(f'Your value in inches is: {convert_cm_to_inches(inch)}in')
        else:
            inch = math.floor(float(untrusted_input.strip()))
             # Check if given value is a positive number greater than 1
            if (not inch > 1):
                raise ValueError("Invalid input!. Value cannot be negative or less than or equal to 1.")
                
            print(f'Your value in inches is: {convert_cm_to_inches(inch)}in')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    centimeters_to_inches()