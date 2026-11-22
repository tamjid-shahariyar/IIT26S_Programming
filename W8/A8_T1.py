########################################################
# Task A8_T1
# Pause
########################################################
import time


def showOptions() -> None:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    return None


def askChoice() -> int:
    Feed = input("Your choice: ")
    try:
        Choice = int(Feed)
    except ValueError:
        Choice = -1
    return Choice


def askDuration() -> float:
    Feed = input("Insert pause duration (s): ")
    try:
        Duration = float(Feed)
    except ValueError:
        print("Invalid duration!")
        Duration = -1.0
    return Duration


def activatePause(PDuration: float) -> None:
    print(f"Pausing for {PDuration} seconds.")
    time.sleep(PDuration)
    print("Unpaused.")
    return None


def main() -> None:
    print("Program starting.")
    Duration = -1.0  # Negative means "not set"
    while True:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            Duration = askDuration()
        elif Choice == 2:
            if Duration < 0:
                print("Pause is not set.")
                print("Set pause first.")
            else:
                activatePause(Duration)
        elif Choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
