def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")
    print(f'#### START "{filename}" ####')
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip("\n"))
    print(f'#### END "{filename}" ####')
    print("Program ending.")


main()
