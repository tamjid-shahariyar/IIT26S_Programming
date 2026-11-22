########################################################
# Task A8_T2
# Calculator
########################################################
import A8_T2_Library as Lib


def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")
    return None


def askChoice() -> int:
    Feed = input("Your choice: ")
    try:
        Choice = int(Feed)
    except ValueError:
        Choice = -1
    return Choice


def askValue(PPrompt: str) -> float:
    while True:
        Feed = input(PPrompt)
        try:
            return float(Feed)
        except ValueError:
            print("Invalid value!")


def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            A = askValue("Insert first addend value: ")
            B = askValue("Insert second addend value: ")
            print(f"{A} + {B} = {Lib.add(A, B)}")
        elif Choice == 2:
            A = askValue("Insert minuend value: ")
            B = askValue("Insert subtrahend value: ")
            print(f"{A} - {B} = {Lib.subtract(A, B)}")
        elif Choice == 3:
            A = askValue("Insert multiplicand value: ")
            B = askValue("Insert multiplier value: ")
            print(f"{A} * {B} = {Lib.multiply(A, B)}")
        elif Choice == 4:
            A = askValue("Insert dividend value: ")
            B = askValue("Insert divisor value: ")
            if B == 0:
                print("Cannot divide by zero!")
            else:
                print(f"{A} / {B} = {Lib.divide(A, B)}")
        elif Choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
