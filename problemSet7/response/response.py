#import validators
from validator_collection import validators, errors

def main():
    print(response(email = input("What's your email address: ")))

def response(email):
    try:
        if validators.email(email) == email:
            return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


main()
