# vowels = ['a','e','i','o','u']
# input_str = input('Input: ')
# output_str=''
# for letter in input_str:
#     if letter.lower() not in vowels:
#         output_str += letter
# print('Output:',output_str)

def main():
    input_str = input('Input: ')
    shorten(input_str)


def shorten(word):
    vowels = ['a','i','e','o','u']
    output_str=''
    for letter in word:
        if letter.lower() not in vowels:
            output_str += letter
    return output_str



if __name__ == "__main__":
    main()
