print("Program starting.")
start_val = int(input("Insert starting value: "))
stop_val = int(input("Insert stopping value: "))

print("Starting while-loop:")
current = start_val
while current <= stop_val:
    if current == stop_val:
        print(current)
    else:
        print(current, end="- ")
    current += 1
print("Program ending.")