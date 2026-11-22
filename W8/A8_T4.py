########################################################
# Task A8_T4
# Years, Months and Weekdays
########################################################
from datetime import datetime
import A8_T4_Library as Lib


def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
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
    Timestamps: list[datetime] = []
    Filename = input("Insert filename: ")
    try:
        Lib.readTimestamps(Filename, Timestamps)
    except FileNotFoundError:
        print(f"File '{Filename}' not found!")
    except ValueError:
        print(f"File '{Filename}' contains invalid timestamps!")
    while True:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            Feed = input("Insert year: ")
            try:
                Year = int(Feed)
                Amount = Lib.calculateYears(Year, Timestamps)
                print(f"Amount of timestamps during year '{Year}' is {Amount}")
            except ValueError:
                print("Invalid year!")
        elif Choice == 2:
            Month = input("Insert month: ")
            Amount = Lib.calculateMonths(Month, Timestamps)
            print(f"Amount of timestamps during month '{Month}' is {Amount}")
        elif Choice == 3:
            Weekday = input("Insert weekday: ")
            Amount = Lib.calculateWeekdays(Weekday, Timestamps)
            print(f"Amount of timestamps during weekday '{Weekday}' is {Amount}")
        elif Choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
