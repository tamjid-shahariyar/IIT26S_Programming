# English alphabets (2 x 26)
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SHIFT = 13


def rot13(text: str) -> str:
    result = ""
    for char in text:
        if char in LOWER_ALPHABETS:
            index = (LOWER_ALPHABETS.index(char) + SHIFT) % len(LOWER_ALPHABETS)
            result += LOWER_ALPHABETS[index]
        elif char in UPPER_ALPHABETS:
            index = (UPPER_ALPHABETS.index(char) + SHIFT) % len(UPPER_ALPHABETS)
            result += UPPER_ALPHABETS[index]
        else:
            result += char
    return result


def collectRows() -> str:
    rows = ""
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        rows += row + "\n"
    return rows


def showText(text: str) -> None:
    print("#### Ciphered text ####")
    print(text, end="")
    print("#### Ciphered text ####")


def saveText(text: str) -> None:
    filename = input("Insert filename to save: ")
    if filename == "":
        print("File name not defined.")
        print("Aborting save operation.")
        return
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    print("Ciphered text saved!")


def main():
    print("Program starting.")
    print("Collecting plain text rows for ciphering.")
    plain_text = collectRows()
    ciphered_text = rot13(plain_text)
    showText(ciphered_text)
    saveText(ciphered_text)
    print("Program ending.")


main()
