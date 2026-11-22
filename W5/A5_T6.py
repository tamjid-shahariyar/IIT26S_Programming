def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None


def askChoice():
    Feed = input("Your choice: ")
    if Feed.isnumeric():
        return int(Feed)
    return -1


def main():
    print("Program starting.")
    Count = 0
    while True:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            print(f"Current count - {Count}")
        elif Choice == 2:
            Count += 1
            print("Count increased!")
        elif Choice == 3:
            Count = 0
            print("Cleared count!")
        elif Choice == 0:
            print("Exiting program.")
            print()
            break
        else:
            print("Unknown option!")
        print()
    print("Program ending.")
    return None


main()
