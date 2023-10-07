s = input('Expression: ').split(' ')
l1 = ['+','-','*']
if(s[1] in l1):
    if(s[1]=='+'):
        print(float(int(s[0])+int(s[2])))
    elif(s[1]=='-'):
        print(float(int(s[0])-int(s[2])))
    elif(s[1]=='*'):
        print(float(int(s[0])*int(s[2])))
elif(s[1]=='/'):
    if(int(s[2])==0):
        pass
    else:
        print(float(int(s[0])/int(s[2])))