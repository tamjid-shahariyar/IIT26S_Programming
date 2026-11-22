########################################################
# Task: template.py
# Generic template for menu-driven programs.
########################################################


def showOptions() -> None:
    print("Options:")
    print("1 - Option one")
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
    while True:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            print("Option one selected.")
        elif Choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
