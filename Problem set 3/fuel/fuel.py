
def get_percentage():
    while True:
        try:
            x,y = get_fraction()
            percentage = round(float((x/y)*100))
            if(x>y):
                raise Exception('')
        except (ZeroDivisionError,Exception):
            pass
        else:
            return percentage
def get_fraction():
    while True:
        try:
            f = input("Fraction: ").split('/')
            x=int(f[0])
            y=int(f[1])
        except ValueError:
            pass
        else:
            return x,y
def main():
     percent = get_percentage()
     if(percent==100 or percent==99):
         print('F')
     elif(percent==0 or percent==1):
         print('E')
     else:
         print(str(percent)+'%')
main()