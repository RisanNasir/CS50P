def check_greetings(greet):
    if "hello" in greet:
        return "$0"
    elif greet[0] == "h":
        return "$20"
    else:
        return "$100"


def main():
    greet = input("Greeting: ")
    reward = check_greetings(greet.lower().strip())
    print(reward)


main()
