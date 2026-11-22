import random
random.seed(1234)

BOT_NAME = "RPS-3PO"
CHOICES = ("rock", "paper", "scissors")

ROCK_ART = """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

PAPER_ART = """    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""

SCISSORS_ART = """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

ARTS = (ROCK_ART, PAPER_ART, SCISSORS_ART)
LINE = "#" * 25

# Result indexes in the stats lists: [wins, losses, draws]
WIN = 0
LOSS = 1
DRAW = 2


def showMenu() -> int:
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    return int(input("Your choice: "))


def showChoice(PName: str, PChoice: int) -> None:
    print("{} chose {}.".format(PName, CHOICES[PChoice - 1]))
    print(ARTS[PChoice - 1])
    return None


def beats(PFirst: int, PSecond: int) -> bool:
    # rock(1) beats scissors(3), paper(2) beats rock(1), scissors(3) beats paper(2)
    return (PFirst == 1 and PSecond == 3) or \
           (PFirst == 2 and PSecond == 1) or \
           (PFirst == 3 and PSecond == 2)


def playRound(PPlayer: str, PPlayerChoice: int,
              PPlayerStats: list[int], PBotStats: list[int]) -> None:
    BotChoice = random.randint(1, 3)
    print("Rock! Paper! Scissors! Shoot!\n")
    print(LINE)
    showChoice(PPlayer, PPlayerChoice)
    print(LINE)
    showChoice(BOT_NAME, BotChoice)
    print(LINE)

    if PPlayerChoice == BotChoice:
        print("Draw! Both players chose {}.".format(CHOICES[BotChoice - 1]))
        PPlayerStats[DRAW] += 1
        PBotStats[DRAW] += 1
    elif beats(PPlayerChoice, BotChoice):
        print("{} {} beats {} {}.".format(PPlayer, CHOICES[PPlayerChoice - 1],
                                          BOT_NAME, CHOICES[BotChoice - 1]))
        PPlayerStats[WIN] += 1
        PBotStats[LOSS] += 1
    else:
        print("{} {} beats {} {}.".format(BOT_NAME, CHOICES[BotChoice - 1],
                                          PPlayer, CHOICES[PPlayerChoice - 1]))
        PBotStats[WIN] += 1
        PPlayerStats[LOSS] += 1
    return None


def showResults(PPlayer: str, PPlayerStats: list[int], PBotStats: list[int]) -> None:
    print("Results:")
    for Name, Stats in ((PPlayer, PPlayerStats), (BOT_NAME, PBotStats)):
        print("{} - wins ({}), losses ({}), draws ({})".format(
            Name, Stats[WIN], Stats[LOSS], Stats[DRAW]))
    return None


def main() -> None:
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    Player = input("Insert player name: ")
    print("Welcome {}!".format(Player))
    print("Your opponent is {}.".format(BOT_NAME))
    print("Game starts...")

    PlayerStats: list[int] = [0, 0, 0]
    BotStats: list[int] = [0, 0, 0]
    while True:
        Choice = showMenu()
        if Choice == 0:
            break
        elif Choice in (1, 2, 3):
            playRound(Player, Choice, PlayerStats, BotStats)
        else:
            print("Unknown option!")

    showResults(Player, PlayerStats, BotStats)
    print("Program ending.")
    return None


main()
