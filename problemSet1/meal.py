def main():
    time = input("What time is it? ")
    tim = convert(time)

    if tim >= 7.0 and tim <= 8.0:
        print("breakfast time")
    elif tim >= 12.0 and tim <= 13.0:
        print("lunch time")
    elif tim >= 18.0 and tim <= 19.0:
        print("dinner time")


def convert(time):
    time = time.split(":")
    min = int(time[1])/60

    tim = int(time[0]) + min

    tim = float(tim)

    return tim


if __name__ == "__main__":
    main()
