import sys, csv

def main():
    if len(sys.argv) <= 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        file1 = sys.argv[1].split(".")
        file2 = sys.argv[2].split(".")
        if (len(file1) == 2 and file1[1] == "csv") and (len(file2) == 2 and file2[1] == "csv"):
            copycsv(sys.argv[1], sys.argv[2])
        else:
            print("Could not read ")
            sys.exit(1)

def copycsv(source, target):
    try:
        with open(target, "w") as targetfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(targetfile, fieldnames=fieldnames)
            writer.writeheader()
            with open(source) as sourcefile:
                reader = csv.DictReader(sourcefile)
                for row in reader:
                    lname, fname = row["name"].split(",")
                    writer.writerow({"first": fname.strip(), "last": lname.strip(), "house": row["house"]})
    except FileNotFoundError:
        print("could not read " + source)
        sys.exit(1)



main()
