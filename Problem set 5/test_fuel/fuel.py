# def get_percentage():
#     while True:
#         try:
#             x,y = get_fraction()
#             percentage = round(float((x/y)*100))
#             if(x>y):
#                 raise Exception('')
#         except (ZeroDivisionError,Exception):
#             pass
#         else:
#             return percentage
# def get_fraction():
#     while True:
#         try:
#             f = input("Fraction: ").split('/')
#             x=int(f[0])
#             y=int(f[1])
#         except ValueError:
#             pass
#         else:
#             return x,y
# def main():
#      percent = get_percentage()
#      if(percent==100 or percent==99):
#          print('F')
#      elif(percent==0 or percent==1):
#          print('E')
#      else:
#          print(str(percent)+'%')
# main()


def main():
    f = input("Fraction: ")
    percentage = convert(f)
    print(gauge(percentage))


def convert(s):
    while True:
        try:
            f = s.split("/")
            x = int(f[0])
            y = int(f[1])
            percentage = round(float((x / y) * 100))
            if x > y:
                raise ValueError
        except (ZeroDivisionError,ValueError):
            raise
        else:
            return percentage


def gauge(percentage):
    if percentage == 100 or percentage == 99:
        return "F"
    elif percentage == 0 or percentage == 1:
        return "E"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
