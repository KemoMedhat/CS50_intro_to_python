import random


def main():
    count = 10
    score = 0
    attemps = 3
    level = get_level()
    while count != 0:
        if attemps == 3:
            x, y = generate_integer(level)
        try:
            user_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if user_answer == answer:
                count = count - 1
                score = score + 1
                attemps = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            attemps = attemps - 1
            pass
        if attemps == 0:
            print((f"{x} + {y} = {answer}"))
            attemps = 3 # Reset attemps to generate new equation
            count = count - 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 4):
                return level
        except (ValueError, Exception):
            pass


def generate_integer(level):
    X, Y = 0, 0
    op = ""
    if level == 1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)

    elif level == 2:
        X = random.randint(10, 99)
        Y = random.randint(10, 99)
    elif level == 3:
        X = random.randint(100, 999)
        Y = random.randint(100, 999)
    return X, Y


if __name__ == "__main__":
    main()
