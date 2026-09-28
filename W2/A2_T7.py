print("Program starting.")

fahrenheit = float(input("Insert fahrenheits: "))

celsius = (fahrenheit - 32) / 1.8
celsius = round(celsius, 1)

print(f"{fahrenheit}°F is {celsius}°C")

print("Program ending.")