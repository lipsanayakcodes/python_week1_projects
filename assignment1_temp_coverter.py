def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

temperature = float(input("Enter temperature: "))

if choice == 1:
    result = celsius_to_fahrenheit(temperature)
    print("Temperature in Fahrenheit:", result)

elif choice == 2:
    result = fahrenheit_to_celsius(temperature)
    print("Temperature in Celsius:", result)

else:
    print("Invalid choice")