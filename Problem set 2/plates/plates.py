def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    NF = False
    FSN = True
    for c in s:
        if c.isdigit():
            NF = True
            if FSN:
                if c == "0":
                    return False
                FSN = False
        elif c.isalpha():
            if NF:
                return False
        else:
            return False
    return True


main()
