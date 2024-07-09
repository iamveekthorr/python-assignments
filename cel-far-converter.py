def evaluate_temperature():
    temp_celsius = float(input("Enter a temperature in Celsius: "))
    
    try:
        if temp_celsius < -273.15:
            return "The temperature is invalid because it is below absolute zero."
        elif temp_celsius == -273.15:
            return "The temperature is absolute zero."
        elif -273.15 < temp_celsius < 0:
            return "The temperature is below freezing."
        elif temp_celsius == 0:
            return "The temperature is at the freezing point."
        elif 0 < temp_celsius < 100:
            return "The temperature is in the normal range."
        elif temp_celsius == 100:
            return "The temperature is at the boiling point."
        elif temp_celsius > 100:
            return "The temperature is above the boiling point."
        else:
            raise ValueError("Invalid input. Please enter a numeric value.")
    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    val = evaluate_temperature()
    print(val)