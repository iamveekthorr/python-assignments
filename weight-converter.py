import re 
import math

'''This function will take in an integer as 
the weight in kilogram (kg) and return an integer'''

def convert_kg_to_pounds(kg: float ) -> float:
    try:
        return math.floor(float(kg * 2.2))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

#  This function is responsible for calculating the weight
def convert_weight():
    try:
        # Get the weigh from the user
        untrusted_input = input("Please enter your weight: ")
        weight = 0
        
        # Regular expression to check for alphabets 
        starts_with_alphabets = re.compile('^[A-Za-z]+$')
        starts_with_alphabets_but_contains_numbers = re.compile('^[A-Za-z].*\d')
        
        # This will check if the user has only entered alphabets
        if (re.match(starts_with_alphabets, untrusted_input) 
           or re.match(starts_with_alphabets_but_contains_numbers, untrusted_input)):
            raise ValueError("Invalid input!. Input must start with a number.")
        
        # first check if the user entered the unit (kg)
        # the strip() function will remove whitespaces anywhere in the input
        if (untrusted_input.__contains__('kg')):
            weight_in_kg = untrusted_input.strip().split('kg')
            print(weight_in_kg[0])
            weight = math.floor(float(weight_in_kg[0]))
            # Check if given value is a positive number greater than 1
            if (not weight > 1):
                raise ValueError("Invalid input!. Weight cannot be negative or less than or equal to 1.")
            
            print(f'Your weight in pounds is: {convert_kg_to_pounds(weight)}lb')
        else:
            weight = math.floor(float(untrusted_input.strip()))
            # Check if given value is a positive number greater than 1
            if (not weight > 1):
                raise ValueError("Invalid input!. Weight cannot be negative or less than or equal to 1.")
            print(f'Your weight in pounds is: {convert_kg_to_pounds(weight)}lb')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    convert_weight()