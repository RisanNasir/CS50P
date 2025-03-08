def main():
    monthlist = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        date = ""
        try:
            date = input("Date: ").strip()
        except EOFError:
            break
        splitdate = date.split()
        if splitdate[0] == date:
            x = date.strip().split('/')
            if x[0].isdigit():
                month = int(x[0])
                day = int(x[1])
                year = int(x[2])
                if month <= 12 and day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break
        else:
            d = date.strip().split()
            dday = d[1]
            if dday[len(d[1])-1] == ',':
                dd = d[1]
                dd = dd.split(',')
                dd = dd[0]
                d[1] = dd

                try:
                    monthindex = monthlist.index(d[0])
                    if monthindex:
                        if int(d[1]) <= 31:
                            print(f"{int(d[2]):04}-{int(monthindex)+1:02}-{int(d[1]):02}")
                            break
                except ValueError:
                    if not (d[0].isalpha() or d[0].isalnum()):
                        break
main()
