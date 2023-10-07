import sys
from datetime import date
import inflect


def main():
    try:
        Birth_date = date.fromisoformat(input("Birth Date: "))
    except ValueError:
        sys.exit("invalid format")
    else:
        print(sing(calcualte_minutes(Birth_date)))


def calcualte_minutes(Birth_date):
    Dayes = str(date.today() - Birth_date).split(" ")
    return int(Dayes[0]) * 24 * 60



def sing(minutes):
    p = inflect.engine()
    words = str(p.number_to_words(minutes).capitalize()).replace("and ", "")
    return words + " minutes"


if __name__ == "__main__":
    main()
