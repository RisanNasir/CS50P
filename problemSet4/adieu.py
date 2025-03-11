def main():
    names = []

    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break

    str = "Adieu, adieu, to"
    i = 0
    for name in names:
        if i == len(names)-1:
            break
        str = str + " " + name + ","
        i += 1

    str = str.rstrip(',')
    if i == 0:
        str += " " + names[i]
    elif i == 1:
        str += " and " + names[i]
    else:
        str += ", and " + names[i]

    print(str)

main()


