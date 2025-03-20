import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    p1 = r'^um| ?\Wum ?|um$'    ##[^a-z0-9., ]+
    p2 = r'um ?|\W+um\W+'
    p3 = r'^um|\W*um\W*'
    p4 = r"\b\W*um\W*\b"
    matches = re.findall(p4, s, re.IGNORECASE)
    #print(len(matches), matches)
    return len(matches)


if __name__ == "__main__":
    main()
