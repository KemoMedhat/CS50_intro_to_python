
def main():
    print('Amount Due: 50')
    Total,Change = 0,0
    Denominations = [5,10,25,50]
    while Total < 50:
        Coin=int(input('Insert Coin: '))
        if Coin in Denominations:
            Total += Coin
        if((50-Total)>0):
            print('Amount Due:',50-Total)

    Change = Total-50
    if(Change >= 0):
        print('Change Owed:',Change)
main()
