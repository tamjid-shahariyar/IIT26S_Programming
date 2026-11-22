def main():
    print("Program starting.")
    print("This program can copy a file.")
    source = input("Insert source filename: ")
    destination = input("Insert destination filename: ")

    print(f"Reading file '{source}' content.")
    with open(source, "r", encoding="utf-8") as file:
        content = file.read()
    print("File content ready in memory.")

    print(f"Writing content into file '{destination}'.")
    with open(destination, "w", encoding="utf-8") as file:
        file.write(content)
    print("Copying operation complete.")
    print("Program ending.")


main()
