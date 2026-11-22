WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)


def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PRows.clear()
    Filehandle = open(PFilename, "r", encoding="utf-8")
    Filehandle.readline()  # skip header row
    while True:
        Line = Filehandle.readline()
        if Line == "":
            break  # end of file
        if Line == "\n":
            continue  # skip empty row
        PRows.append(Line.rstrip("\n"))
    Filehandle.close()
    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(PRows)):
        for j in range(len(WEEKDAYS)):
            if PRows[i].startswith(WEEKDAYS[j]):
                WeekdayTimestampAmount[j] += 1
    for i in range(len(WEEKDAYS)):
        PResults.append(" - {} {} stamps".format(WEEKDAYS[i], WeekdayTimestampAmount[i]))
    WeekdayTimestampAmount.clear()
    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for Result in PResults:
        print(Result)
    print("### Timestamp analysis ###")
    return None


def main() -> None:
    print("Program starting.")
    Rows: list[str] = []
    Results: list[str] = []
    Filename = input("Insert filename: ")
    readFile(Filename, Rows)
    analyseTimestamps(Rows, Results)
    displayResults(Results)
    Rows.clear()
    Results.clear()
    print("Program ending.")
    return None


main()
