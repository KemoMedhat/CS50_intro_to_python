import random

while True:
    try:
        level = int(input("Level: "))
        num = random.randint(1, level)
        while True:
            try:
                n = int(input("Guess: "))
            except ValueError:
                pass
            else:
                if n < num:
                    print("Too small!")
                elif n > num:
                    print("Too large!")
                elif n == num:
                    print("Just right!")
                    break
    except ValueError:
        pass
    else:
        break
