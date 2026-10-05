print("Program starting.")
print("Check multiplicative persistence.")
num_str = input("Insert an integer: ")

steps = 0

while len(num_str) > 1:
    product = 1
    step_display = ""
    
    for i, digit in enumerate(num_str):
        product *= int(digit)
        if i == len(num_str) - 1:
            step_display += digit
        else:
            step_display += digit + "\\*"
    
    if steps == 0:
        print(f"{step_display}- {product}")
    else:
        print(f"{step_display} = {product}")
    
    num_str = str(product)
    steps += 1

print("No more steps.")
print(f"\nThis program took {steps} step(s)")
print("\nProgram ending.")