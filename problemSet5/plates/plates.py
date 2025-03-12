def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    is_numbers_rule(s)
    if len(s) >= 2 and len(s) <= 6 and is_first_two_letters(s) and is_no_punctuation(s) and is_numbers_rule(s):
        return True
    else:
        return False


def is_first_two_letters(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False

def is_no_punctuation(s):
    return s.isalnum()

def is_numbers_rule(s):
    digitrule = True
    middle_number = True
    i = 0

    for d in s:
        if d.isdigit() and d == "0" :
            digitrule = False
            break
        elif d.isdigit() and d != "0":
            digitrule = True
            break
        i += 1

    while i < len(s):
        if s[i].isalpha():
            middle_number = False
            break
        else:
            middle_number = True
        i += 1

    return digitrule and middle_number

main()
