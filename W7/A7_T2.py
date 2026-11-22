SEPARATOR = ","


def parseValues(PText: str, PIntegers: list[int]) -> None:
    for Value in PText.split(SEPARATOR):
        try:
            PIntegers.append(int(Value))
        except ValueError:
            print("Invalid value '{}' detected.".format(Value))
    return None


def analyseIntegers(PIntegers: list[int]) -> None:
    if len(PIntegers) == 0:
        print("No values to analyse.")
        return None
    Total = 0
    for Value in PIntegers:
        Total += Value
    Parity = "even" if Total % 2 == 0 else "odd"
    print("There are {} integers in the list.".format(len(PIntegers)))
    print("Sum of the integers is {} and it's {}".format(Total, Parity))
    return None


def main() -> None:
    print("Program starting.")
    Integers: list[int] = []
    Text = input("Insert comma separated integers: ")
    parseValues(Text, Integers)
    analyseIntegers(Integers)
    Integers.clear()
    print("Program ending.")
    return None


main()
