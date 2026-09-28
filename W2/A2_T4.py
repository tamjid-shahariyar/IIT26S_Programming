print("Program starting.")
print("Estimate how many minutes you spent on programming...")
print()

a1 = int(input("A1_T1: "))
a2 = int(input("A1_T2: "))
a3 = int(input("A1_T3: "))
a4 = int(input("A1_T4: "))
a5 = int(input("A1_T5: "))
a6 = int(input("A1_T6: "))
a7 = int(input("A1_T7: "))

total = a1 + a2 + a3 + a4 + a5 + a6 + a7
average = total / 7
average_rounded = round(average, 2)
average_integer = int(round(average, 0))

print()
print(f"In total you spent {total} minutes on programming.")
print(f"Average per task was {average_rounded} min and same rounded to the nearest integer {average_integer} min.")

print()
print("Program ending.")