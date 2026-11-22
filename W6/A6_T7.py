PROGRESS_FILE = "player_progress.txt"
SEPARATOR = ";"
LOCATIONS = ["home", "Galba's palace", "Otho's palace",
             "Vitellius' palace", "Vespasian's palace"]

# English alphabets (2 x 26)
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SHIFT = 13


def rot13(text: str) -> str:
    result = ""
    for char in text:
        if char in LOWER_ALPHABETS:
            result += LOWER_ALPHABETS[(LOWER_ALPHABETS.index(char) + SHIFT) % 26]
        elif char in UPPER_ALPHABETS:
            result += UPPER_ALPHABETS[(UPPER_ALPHABETS.index(char) + SHIFT) % 26]
        else:
            result += char
    return result


def readProgress() -> str:
    """Return the latest progress row: current;next;passphrase (ciphered)."""
    last_row = ""
    with open(PROGRESS_FILE, "r", encoding="utf-8") as file:
        file.readline()  # skip header row
        for line in file:
            row = line.strip()
            if row != "":
                last_row = row
    return last_row


def saveProgress(row: str) -> None:
    with open(PROGRESS_FILE, "a", encoding="utf-8") as file:
        file.write(row.strip() + "\n")
    print("[Game] Progress autosaved!")


def readMessage(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def saveMessage(filename: str, text: str) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


def main():
    print("Travel starting.")
    progress = readProgress().split(SEPARATOR)
    current_id = int(progress[0])
    next_id = int(progress[1])
    ciphered_pass = progress[2]
    plain_pass = rot13(ciphered_pass)

    print(f"Currently at {LOCATIONS[current_id]}.")
    print(f"Travelling to {LOCATIONS[next_id]}...")
    print(f"...Arriving to the {LOCATIONS[next_id]}.")
    print("Passing the guard at the entrance.")
    print(f'"{plain_pass.capitalize()}!"')

    print("Looking for the message in the palace...")
    message = readMessage(f"{next_id}_{ciphered_pass}.gkg")
    print("Ah, there it is! Seems cryptic.")

    first_line, _, rest = message.partition("\n")
    saveProgress(first_line)

    print("Deciphering Emperor's message...")
    saveMessage(f"{next_id}-{plain_pass}.txt", rot13(rest))
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")


main()
