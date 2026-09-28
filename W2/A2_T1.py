print("Program starting.")
Name = input("What is your name: ")
Num1 = float(input("Enter a floating point number: "))
Num2 = float(input("Enter second floating point number: "))

Product = Num1 * Num2
Product = round(Product, 2)

print(Name, "you gave numbers", Num1, "and", Num2)
print("Multiplying first and second number will result in product", Product)
print("Program ending.")