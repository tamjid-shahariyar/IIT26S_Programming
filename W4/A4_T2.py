print("Program starting.")
start_val = int(input("Insert starting value: "))
stop_val = int(input("Insert stopping value: "))

print("Starting for-loop:")
for i in range(start_val, stop_val + 1):
    if i == stop_val:
        print(i) 
    else:
        print(i, end="-")
print("Program ending.")