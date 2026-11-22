DELIMITER = ","


def collectWords():
    Words = ""
    while True:
        Word = input("Insert word(empty stops): ")
        if Word == "":
            break
        if Words == "":
            Words = Word
        else:
            Words = Words + DELIMITER + Word
    return Words


def analyseWords(PWords):
    if PWords == "":
        WordList = []
    else:
        WordList = PWords.split(DELIMITER)
    WordCount = len(WordList)
    CharCount = 0
    for Word in WordList:
        CharCount += len(Word)
    if WordCount > 0:
        Avg = CharCount / WordCount
    else:
        Avg = 0
    print(f"- {WordCount} Words")
    print(f"- {CharCount} Characters")
    print("- {:.2f} Average word length".format(Avg))
    return None


def main():
    print("Program starting.")
    Words = collectWords()
    analyseWords(Words)
    print("Program ending.")
    return None


main()
