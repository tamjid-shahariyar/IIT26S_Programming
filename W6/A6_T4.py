SEPARATOR = ";"


def readNames(filename: str) -> str:
    names = ""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name = line.strip()
            if name == "":
                continue  # skip empty rows
            if names != "":
                names += SEPARATOR
            names += name
    return names


def analyseNames(names: str) -> str:
    count = 0
    total_length = 0
    shortest = 0
    longest = 0
    for name in names.split(SEPARATOR):
        length = len(name)
        if count == 0 or length < shortest:
            shortest = length
        if count == 0 or length > longest:
            longest = length
        total_length += length
        count += 1
    average = total_length / count if count > 0 else 0.0

    report = "#### REPORT BEGIN ####\n"
    report += "Name count - {}\n".format(count)
    report += "Shortest name - {} chars\n".format(shortest)
    report += "Longest name - {} chars\n".format(longest)
    report += "Average name - {:.2f} chars\n".format(average)
    report += "#### REPORT END ####"
    return report


def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ")
    print(f'Reading names from "{filename}".')
    names = readNames(filename)
    print("Analysing names...")
    report = analyseNames(names)
    print("Analysis complete!")
    print(report)
    print("Program ending.")


main()
