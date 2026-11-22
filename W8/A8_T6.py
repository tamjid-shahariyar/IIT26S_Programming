########################################################
# Task A8_T6
# Scalable Vector Graphics
# Requires: pip install svgwrite==1.4.3
########################################################
import svgwrite
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle


def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")
    return None


def askChoice() -> int:
    Feed = input("Your choice: ")
    try:
        Choice = int(Feed)
    except ValueError:
        Choice = -1
    return Choice


def askValue(PPrompt: str) -> float:
    while True:
        Feed = input(PPrompt)
        try:
            return float(Feed)
        except ValueError:
            print("Invalid value!")


def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    Left = askValue("- Left edge position: ")
    Top = askValue("- Top edge position: ")
    Side = askValue("- Side length: ")
    Fill = input("- Fill color: ")
    Stroke = input("- Stroke color: ")
    PDwg.add(Rect(insert=(Left, Top), size=(Side, Side), fill=Fill, stroke=Stroke))
    return None


def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    CenterX = askValue("- Center X coord: ")
    CenterY = askValue("- Center Y coord: ")
    Radius = askValue("- Radius: ")
    Fill = input("- Fill color: ")
    Stroke = input("- Stroke color: ")
    PDwg.add(Circle(center=(CenterX, CenterY), r=Radius, fill=Fill, stroke=Stroke))
    return None


def saveSvg(PDwg: Drawing) -> None:
    Filename = input("Insert filename: ")
    print(f'Saving file to "{Filename}"')
    Proceed = input("Proceed (y/n)?: ")
    if Proceed.strip().lower() == "y":
        PDwg.saveas(Filename, pretty=True, indent=2)
        print("Vector saved successfully!")
    else:
        print("Saving cancelled.")
    return None


def main() -> None:
    # 1. Initialise
    print("Program starting.")
    Dwg = svgwrite.Drawing()
    # 2. Operate
    while True:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            drawSquare(Dwg)
        elif Choice == 2:
            drawCircle(Dwg)
        elif Choice == 3:
            saveSvg(Dwg)
        elif Choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
    # 3. Cleanup
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
