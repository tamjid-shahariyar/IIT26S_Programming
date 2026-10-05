print("Program starting.")
num = int(input("Insert a positive integer: "))

original_num = num
steps = 0
output = str(num)

while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3 * num + 1
    steps += 1
    output += f"- >{num}"

print(f"{output} Sequence had {steps} total steps.")