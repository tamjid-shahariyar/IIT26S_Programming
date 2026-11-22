########################################################
# Task A8_T3 - Library
# Number file analysis
########################################################


def readValues(PFilename: str, PValues: list[float]) -> None:
    PValues.clear()
    with open(PFilename, "r", encoding="UTF-8") as Filehandle:
        for Row in Filehandle:
            Row = Row.strip()
            if Row == "":
                continue
            PValues.append(float(Row))
    return None


def calculateSum(PValues: list[float]) -> float:
    Total = 0.0
    for Value in PValues:
        Total += Value
    return round(Total, 1)


def calculateAverage(PValues: list[float]) -> float:
    if len(PValues) == 0:
        return 0.0
    Total = 0.0
    for Value in PValues:
        Total += Value
    return round(Total / len(PValues), 1)
