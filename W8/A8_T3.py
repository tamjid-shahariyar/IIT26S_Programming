########################################################
# Task A8_T3
# Number files
########################################################
import A8_T3_Library as Lib


def showOptions() -> None:
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")
    return None


def askChoice() -> int:
    Feed = input("Your choice: ")
    try:
        Choice = int(Feed)
    except ValueError:
        Choice = -1
    return Choice


def main() -> None:
    print("Program starting.")
    Values: list[float] = []
    while True:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            Filename = input("Insert filename: ")
            try:
                Lib.readValues(Filename, Values)
            except FileNotFoundError:
                print(f"File '{Filename}' not found!")
            except ValueError:
                print(f"File '{Filename}' contains invalid values!")
                Values.clear()
        elif Choice == 2:
            print(f"Amount of values {len(Values)}")
        elif Choice == 3:
            print(f"Sum of values {Lib.calculateSum(Values)}")
        elif Choice == 4:
            print(f"Average of values {Lib.calculateAverage(Values)}")
        elif Choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
