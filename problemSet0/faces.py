def convert(phrase):
    phrase = phrase.replace(":)","🙂")
    phrase = phrase.replace(":(","🙁")
    print(phrase)


def main():
    phrase = input()
    convert(phrase)

main()
