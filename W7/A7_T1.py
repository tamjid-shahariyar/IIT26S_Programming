def collectIntegers(PIntegers: list[int]) -> None:
    print("Collect positive integers.")
    while True:
        Value = int(input("Insert positive integer(negative stops): "))
        if Value < 0:
            break
        PIntegers.append(Value)
    print("Stopped collecting positive integers.")
    return None


def displayIntegers(PIntegers: list[int]) -> None:
    if len(PIntegers) == 0:
        print("No integers to display.")
        return None
    print("Displaying {} integers:".format(len(PIntegers)))
    for i in range(len(PIntegers)):
        print("- Index {} => Ordinal {} => Integer {}".format(i, i + 1, PIntegers[i]))
    return None


def main() -> None:
    print("Program starting.")
    Integers: list[int] = []
    collectIntegers(Integers)
    displayIntegers(Integers)
    Integers.clear()
    print("Program ending.")
    return None


main()
