########################################################
# Task A8_T5 - Library
# Login and register
########################################################
import hashlib
import os

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hashPassword(PPassword: str) -> str:
    return hashlib.md5(PPassword.encode("UTF-8")).hexdigest()


def readCredentials() -> list[list[str]]:
    Credentials: list[list[str]] = []
    if not os.path.exists(CREDENTIALS_FILE):
        return Credentials
    with open(CREDENTIALS_FILE, "r", encoding="UTF-8") as Filehandle:
        for Row in Filehandle:
            Row = Row.strip()
            if Row == "":
                continue
            Columns = Row.split(DELIMITER)
            if len(Columns) == 3:
                Credentials.append(Columns)
    return Credentials


def registerUser(PUsername: str, PPassword: str) -> None:
    Credentials = readCredentials()
    NewId = len(Credentials)
    PasswordHash = hashPassword(PPassword)
    with open(CREDENTIALS_FILE, "a", encoding="UTF-8") as Filehandle:
        Filehandle.write(f"{NewId}{DELIMITER}{PUsername}{DELIMITER}{PasswordHash}\n")
    return None


def loginUser(PUsername: str, PPassword: str) -> list[str]:
    """Returns [id, username] on success, empty list on failure."""
    PasswordHash = hashPassword(PPassword)
    for Columns in readCredentials():
        if Columns[1] == PUsername and Columns[2] == PasswordHash:
            return [Columns[0], Columns[1]]
    return []
