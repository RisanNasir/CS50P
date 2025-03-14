import sys

def main():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        readFile(sys.argv[1])

def readFile(fileName):
    fullName = fileName.split('.')
    if len(fullName) < 2:
        print("File does not exist")
        sys.exit(1)
    elif len(fullName) == 2 and fullName[1] != 'py':
        print("Not a Python file")
        sys.exit(1)
    try:
        with open(fileName) as file:
            linesofcode = 0
            for line in file:
                if(checkLine(line)):
                    linesofcode += 1
            print(linesofcode)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

def checkLine(line):
    if not (line.lstrip().startswith(("\n", "#", "'''", "help"," ")) or line.isspace()):
        return True
    else:
        return False
main()
