def main():
    variable_name = input("camelCase: ")
    print(convert_to_snakecase(variable_name))

def convert_to_snakecase(name):
    snake_case = ""
    for c in name:
        if (c.isupper()):
            snake_case += "_"
        snake_case += c.lower()

    return snake_case


main()
