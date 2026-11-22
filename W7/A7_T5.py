from dataclasses import dataclass

DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)


@dataclass
class TIMESTAMP:
    weekday: str = ""
    hour: int = 0
    consumption: float = 0.0
    price: float = 0.0


@dataclass
class DAY_USAGE:
    weekday: str = ""
    usage: float = 0.0
    cost: float = 0.0


def readTimestamps(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PTimestamps.clear()
    with open(PFilename, "r", encoding="utf-8") as Filehandle:
        Filehandle.readline()  # skip header row
        for Line in Filehandle:
            Row = Line.rstrip()
            if Row == "":
                continue
            Columns = Row.split(DELIMITER)
            Timestamp = TIMESTAMP()
            Timestamp.weekday = Columns[0]
            Timestamp.hour = int(Columns[1])
            Timestamp.consumption = float(Columns[2])
            Timestamp.price = float(Columns[3])
            PTimestamps.append(Timestamp)
            Columns.clear()
    return None


def analyseTimestamps(PTimestamps: list[TIMESTAMP], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    DayUsages: list[DAY_USAGE] = []
    for Weekday in WEEKDAYS:
        DayUsages.append(DAY_USAGE(Weekday))

    for Timestamp in PTimestamps:
        for DayUsage in DayUsages:
            if Timestamp.weekday == DayUsage.weekday:
                DayUsage.usage += Timestamp.consumption
                DayUsage.cost += Timestamp.consumption * Timestamp.price

    for DayUsage in DayUsages:
        PResults.append(" - {} usage {:.2f} kWh, cost {:.2f} €".format(
            DayUsage.weekday, DayUsage.usage, DayUsage.cost))
    DayUsages.clear()
    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for Result in PResults:
        print(Result)
    print("### Electricity consumption summary ###")
    return None


def main() -> None:
    print("Program starting.")
    Timestamps: list[TIMESTAMP] = []
    Results: list[str] = []
    Filename = input("Insert filename: ")
    readTimestamps(Filename, Timestamps)
    analyseTimestamps(Timestamps, Results)
    displayResults(Results)
    Timestamps.clear()
    Results.clear()
    print("Program ending.")
    return None


main()
