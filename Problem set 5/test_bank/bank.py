# greating = input('Greeting: ').strip()
# if(greating[0].lower()=='h'):
#     if(greating[0:5].lower()=='hello'):
#         print('$0')
#     else:
#         print('$20')
# else:
#         print('$100')



def main():
    print(value(input('Greeting: ').strip()))


def value(greeting):
    if(greeting[0].lower()=='h'):
        if(greeting[0:5].lower()=='hello'):
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()