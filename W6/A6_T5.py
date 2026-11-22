SEPARATOR = ";"


def readValues(filename: str) -> str:
    values = ""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            row = line.strip()
            if row == "":
                continue
            if values != "":
                values += SEPARATOR
            values += row
    return values


def analyseNumbers(values: str) -> str:
    count = 0
    total = 0
    greatest = 0
    if values != "":
        for value in values.split(SEPARATOR):
            number = int(value)
            if count == 0 or number > greatest:
                greatest = number
            total += number
            count += 1
    average = total / count if count > 0 else 0.0
    return "{}{}{}{}{}{}{:.2f}".format(
        count, SEPARATOR, total, SEPARATOR, greatest, SEPARATOR, average)


def displayResults(filename: str, results: str) -> None:
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")
    print(results)
    print("#### Number analysis - END ####")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    results = analyseNumbers(values)
    displayResults(filename, results)
    print("Program ending.")


main()
