import random, sys

def main():

    while True:
        level = input("Level: ")
        if level.isnumeric() and level != '0':
            level = int(level)
            break
    randomNumber = random.randint(1, level)

    while True:
        guess = input("Guess: ")
        if guess.isnumeric() : ##and int(guess) < int(level)
            guess = int(guess)
            if guess < randomNumber:
                print("Too small!")
            elif guess > randomNumber:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit(0)

main()
