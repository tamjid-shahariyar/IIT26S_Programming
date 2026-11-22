print("Program starting.")
print("Check multiplicative persistence.")
num_str = input("Insert an integer: ")

steps = 0

while len(num_str) > 1:
    product = 1
    for digit in num_str:
        product *= int(digit)

    print(f"{'*'.join(num_str)} = {product}")

    num_str = str(product)
    steps += 1

print("No more steps.")
print(f"\nThis program took {steps} step(s)")
print("\nProgram ending.")
