import re
import sys


def main():
    print(parse(str(input("HTML: "))))

def parse(sss):
    matche = re.search(r"https?://(www\.)?youtube\.com/embed/(\w+)\"",sss)
    return (f"https://youtu.be/{matche.group(2)}") if matche else None


if __name__ == "__main__":
    main()