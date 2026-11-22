from dataclasses import dataclass

DELIMITER = ";"


@dataclass
class TIMESTAMP:
    weekday: str = ""
    hour: int = 0
    consumption: float = 0.0
    price: float = 0.0


def readTimestamps(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PTimestamps.clear()
    with open(PFilename, "r", encoding="utf-8") as Filehandle:
        Filehandle.readline()  # skip header row
        for Line in Filehandle:
            Row = Line.rstrip()  # Remove newline
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


def displayTimestamps(PTimestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for Timestamp in PTimestamps:
        Total = Timestamp.consumption * Timestamp.price
        print(" - {} {:02d}:00, price {:.2f}, consumption {:.2f} kWh, total {:.2f} €".format(
            Timestamp.weekday, Timestamp.hour, Timestamp.price,
            Timestamp.consumption, Total))
    return None


def main() -> None:
    print("Program starting.")
    Timestamps: list[TIMESTAMP] = []
    Filename = input("Insert filename: ")
    readTimestamps(Filename, Timestamps)
    displayTimestamps(Timestamps)
    Timestamps.clear()
    print("Program ending.")
    return None


main()
