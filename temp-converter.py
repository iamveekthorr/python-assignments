def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    try:
        # Ask the user for a temperature
        temp = float(input("Enter the temperature: "))

        # Ask the user for the units
        units = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Convert and print the result based on the units
        if units == "C":
            converted_temp = celsius_to_fahrenheit(temp)
            print(f"{temp} degrees Celsius is {converted_temp:.2f} degrees Fahrenheit.")
        elif units == "F":
            converted_temp = fahrenheit_to_celsius(temp)
            print(f"{temp} degrees Fahrenheit is {converted_temp:.2f} degrees Celsius.")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the temperature.")
        
if __name__ == '__main__':
    temperature_converter()