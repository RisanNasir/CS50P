import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if (len(sys.argv) != 3 and len(sys.argv) != 1) or (sys.argv[1] != '-f'):
        print("Invalid usage")
        sys.exit(1)
    elif len(sys.argv) == 1:
        selectedFont = random.choices(fonts, k=1)
        figlet.setFont(font = selectedFont[0] )

    try:
        fonts.index(sys.argv[2])
        figlet.setFont(font = sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)

    str = input("Input: ")
    print(figlet.renderText(str))



main()
