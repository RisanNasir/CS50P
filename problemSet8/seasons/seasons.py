import sys
from datetime import date
from datetime import timedelta
import inflect


def main():
    str = into_minutes(input("Date of Birth: "))
    if str == "Invalid date":
            print(str)
            sys.exit(1)
    print(str)


def into_minutes(dob):
    try:
        dob = date.fromisoformat(dob)
        delta = date.today() - dob
        p = inflect.engine()
        count = round(delta.total_seconds()/60)
        return p.number_to_words(count, andword="").capitalize() + ' ' + p.plural_noun('minute', count)
    except ValueError:
         return "Invalid date"


if __name__ == "__main__":
    main()
