########################################################
# Task A8_T5
# Login and register
########################################################
import A8_T5_Library as Lib


def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")
    return None


def showUserOptions() -> None:
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")
    return None


def askChoice() -> int:
    Feed = input("Your choice: ")
    try:
        Choice = int(Feed)
    except ValueError:
        Choice = -1
    return Choice


def userMenu(PUser: list[str]) -> None:
    while True:
        showUserOptions()
        Choice = askChoice()
        if Choice == 1:
            print(f"Profile ID {PUser[0]} - {PUser[1]}")
        elif Choice == 2:
            print("Feature not implemented.")
        elif Choice == 0:
            print("Logging out...")
            break
        else:
            print("Unknown option!")
    return None


def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            Username = input("Insert username: ")
            Password = input("Insert password: ")
            User = Lib.loginUser(Username, Password)
            if User:
                print("Authentication successful!")
                userMenu(User)
            else:
                print("Authentication failed!")
        elif Choice == 2:
            Username = input("Insert username: ")
            Password = input("Insert password: ")
            Lib.registerUser(Username, Password)
            print("User registration completed!")
        elif Choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
