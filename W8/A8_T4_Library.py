########################################################
# Task A8_T4 - Library
# Timestamp counting
########################################################
from datetime import datetime

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M"


def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    PTimestamps.clear()
    with open(PFilename, "r", encoding="UTF-8") as Filehandle:
        for Row in Filehandle:
            Row = Row.strip()
            if Row == "":
                continue
            PTimestamps.append(datetime.strptime(Row, TIMESTAMP_FORMAT))
    return None


def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    Count = 0
    for Timestamp in PTimestamps:
        if Timestamp.year == PYear:
            Count += 1
    return Count


def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    if PMonth not in MONTHS:
        return 0
    MonthNumber = MONTHS.index(PMonth) + 1  # datetime months are 1-12
    Count = 0
    for Timestamp in PTimestamps:
        if Timestamp.month == MonthNumber:
            Count += 1
    return Count


def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    if PWeekday not in WEEKDAYS:
        return 0
    WeekdayNumber = WEEKDAYS.index(PWeekday)  # weekday(): Monday == 0
    Count = 0
    for Timestamp in PTimestamps:
        if Timestamp.weekday() == WeekdayNumber:
            Count += 1
    return Count
