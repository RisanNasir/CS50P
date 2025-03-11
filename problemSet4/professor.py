import random


def main():

    level = get_level()
    count = 0
    userScore = 0
    result = 0
    while count < 10:
        x = int(generate_integer(level))
        y = int(generate_integer(level))

        i = 0
        while i < 3:
            result = input(f"{x} + {y} = ")

            if result.isnumeric() and int(result) == (x + y):
                userScore += 1
                break
            i += 1
            print("EEE")

        if  (not result.isnumeric() or not int(result) == x + y ):
            print(f"{x} + {y} = {x + y}")

        count += 1

    print("Score: ", userScore)

def get_level():

    while True:
        level = input("Level: ")
        if level == '1' or level == '2' or level == '3':
            return level


def generate_integer(level):
    if level == '1':
        level = 9
        return random.randint(0, int(level))
    elif level == '2':
        level = 99
        return random.randint(10, int(level))
    elif level == '3':
        level = 999
        return random.randint(100, int(level))



if __name__ == "__main__":
    main()
