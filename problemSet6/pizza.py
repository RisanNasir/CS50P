import sys
from tabulate import tabulate

def main():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        try:
            if not sys.argv[1].split(".")[1] == "csv":
                sys.exit(1)
            else:
                fetchFile(sys.argv[1])
        except IndexError:
                sys.exit(1)

def fetchFile(name):
    with open(name) as file:
        lines = []
        for line in file:
            lines.append(line.split(","))
        lines[0][2] = lines[0][2].strip("\n")
        headers = lines[0]
        lines.remove(lines[0])
        print(tabulate(lines,headers,tablefmt="grid"))
       

main()
