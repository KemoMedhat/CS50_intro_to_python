grocery_list={}
while True:
    try:
        item = input().lower()
    except EOFError:
        break
    else:
        if(item not in grocery_list.keys()):
            grocery_list[item]=1
        else:
            grocery_list[item] +=1
for i in sorted(grocery_list):
    print(grocery_list[i],i.upper())