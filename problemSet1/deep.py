def great_question(answer):
    answer = answer.lower().strip()
    if answer == "42" or answer == "forty two" or answer == "forty-two":
        return "Yes"
    else:
        return "No"

def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print(great_question(answer))

main()
