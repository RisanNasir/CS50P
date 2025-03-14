import sys
from PIL import Image, ImageFilter, ImageDraw, ImageOps

def main():
    if len(sys.argv) <= 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    source = sys.argv[1].split(".")
    target = sys.argv[2].split(".")
    ext = " jpg jpeg png "

    ##print(source, target)
    if (len(source) != 2 or len(target) != 2):
        print("Invalid output")
        sys.exit(1)
    elif source[1].lower() != target[1].lower():
        print("Input and output have different extensions")
        sys.exit(1)
    elif (not ext.find(source[1].lower())) or (not ext.find(target[1].lower())):
        print("Invalid output")
        exit(1)

    putonshirt(sys.argv[1], sys.argv[2])


def putonshirt(source, target):
    ## "i'm putting on cs50 shirt"
    try:

        muppet = Image.open(source)
        shirt = Image.open("shirt.png")
        extra1 = muppet.copy()

        extra1 = ImageOps.fit(muppet, shirt.size)
        extra1.paste(shirt,shirt)
        extra1.save(target)

    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)


main()
