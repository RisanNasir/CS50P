import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    splited = ip.split(".")
    if len(splited) != 4:
        return False
    flag = False
    for no in splited:
        if int(no) >=0 and int(no) <= 255:
            flag = True
        else:
            return False

    return flag

if __name__ == "__main__":
    main()
