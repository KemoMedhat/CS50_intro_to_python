def main():
    time=convert(input('What time is it? '))
    if(time >= 7.0 and time < 8.1):
        print('breakfast time')
    elif(time >= 12.0 and time < 13.1):
        print('lunch time')
    elif(time >= 18.0 and time < 19.1):
        print('dinner time')

def convert(time):
    tmp=time.split(':')
    tmp[1]=str(int(tmp[1])/60)
    return float(tmp[0])+float(tmp[1])


if __name__ == "__main__":
    main()