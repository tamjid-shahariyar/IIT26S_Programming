print("Program starting.")
start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))

valid = True
if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    valid = False
if inspect < start or inspect > stop:
    print("Inspection value must be within the range of start and stop.")
    valid = False

if valid:
    print("First loop - inspection with break:")
    for i in range(start, stop + 1):
        if i == inspect:
            break
        if i == stop:
            print(i)
        else:
            print(i, end=".")
            
    print("\nSecond loop - inspection with continue:")
    for i in range(start, stop + 1):
        if i == inspect:
            continue
        if i == stop:
            print(i)
        else:
            print(i, end=".")
    print()

print("Program ending.")