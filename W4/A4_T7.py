print("Program starting.")
print("Check multiplicative persistence.")
num_str = input("Insert an integer: ")

steps = 0

# Continue while the number has more than 1 digit
while len(num_str) > 1:
    product = 1
    step_display = ""
    
    # Build the display string (e.g., "2\*7\*7...")
    for i, digit in enumerate(num_str):
        product *= int(digit)
        if i == len(num_str) - 1:
            step_display += digit
        else:
            step_display += digit + "\\*"
    
    # Print the step line with the required format
    if steps == 0:
        print(f"{step_display}- {product}")
    else:
        print(f"{step_display} = {product}")
    
    num_str = str(product)
    steps += 1

print("No more steps.")
print(f"\nThis program took {steps} step(s)")
print("\nProgram ending.")