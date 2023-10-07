ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if(ans.strip().isdigit()):
    if(int(ans)==42):
        print('Yes')
    else:
        print('No')
elif(ans.lower()=='forty two' or ans.lower()=='forty-two'):
    print('Yes')
else:
    print('No')