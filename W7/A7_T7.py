ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CONFIG_SEPARATOR = ":"


def readConfig(PFilename: str, PRotors: list[str]) -> str:
    """Read rotors into PRotors and return the reflector."""
    PRotors.clear()
    Reflector = ""
    with open(PFilename, "r", encoding="utf-8") as Filehandle:
        for Line in Filehandle:
            Row = Line.strip()
            if Row == "":
                continue
            Key, Value = Row.split(CONFIG_SEPARATOR)
            if Key.startswith("Rotor"):
                PRotors.append(Value)
            elif Key == "Reflector":
                Reflector = Value
    return Reflector


def askPlugs() -> None:
    Answer = input("Insert plugs (y/n)?: ")
    if Answer.lower() == "y":
        print("Plugboard not implemented. No extra plugs inserted.")
    else:
        print("No extra plugs inserted.")
    return None


def rotateRotors(PPositions: list[int], PRotors: list[str]) -> None:
    PPositions[0] = (PPositions[0] + 1) % len(PRotors[0])
    if PPositions[0] == 0:
        PPositions[1] = (PPositions[1] + 1) % len(PRotors[1])
        if PPositions[1] == 0:
            PPositions[2] = (PPositions[2] + 1) % len(PRotors[2])
    return None


def scrambleChar(PChar: str, PPositions: list[int], PRotors: list[str], PReflector: str) -> str:
    Size = len(ALPHABETS)
    rotateRotors(PPositions, PRotors)
    Index = ALPHABETS.index(PChar)

    # Forward pass-through, rotors 1-3
    for i in range(len(PRotors)):
        Offset = (Index + PPositions[i]) % Size
        Index = (PRotors[i].index(ALPHABETS[Offset]) - PPositions[i]) % Size

    # Reflector
    Index = ALPHABETS.index(PReflector[Index])

    # Reverse pass-through, rotors 3-1
    for i in range(len(PRotors) - 1, -1, -1):
        Offset = (PPositions[i] + Index) % Size
        Index = (ALPHABETS.index(PRotors[i][Offset]) - PPositions[i]) % Size

    return ALPHABETS[Index]


def convertRow(PRow: str, PRotors: list[str], PReflector: str) -> str:
    Positions: list[int] = [0, 0, 0]  # reset rotors for every row
    Converted = ""
    for Char in PRow:
        Upper = Char.upper()
        if Upper in ALPHABETS:
            Result = scrambleChar(Upper, Positions, PRotors, PReflector)
        else:
            Result = Char
        print('Character "{}" illuminated as "{}"'.format(Char, Result))
        Converted += Result
    Positions.clear()
    return Converted


def main() -> None:
    Rotors: list[str] = []
    Filename = input("Insert config(filename): ")
    Reflector = readConfig(Filename, Rotors)
    askPlugs()
    print("Enigma initialized.")
    while True:
        Row = input("Insert row (empty stops): ")
        if Row == "":
            break
        Converted = convertRow(Row, Rotors, Reflector)
        print('Converted row - "{}".'.format(Converted))
    print("Enigma closing.")
    Rotors.clear()
    return None


main()
