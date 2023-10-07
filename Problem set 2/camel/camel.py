def main():
    CamelCase=input('camelCase: ')
    print('snake_case:',snake_case(CamelCase))

def snake_case(CamelCase):
    tmp_list = []
    tmp_str = ''
    for c in CamelCase:
        tmp_list.append(c)
    for i,j in enumerate(tmp_list):
        if(j.isupper() and i != 0):
            tmp_str += '_'+j
        else:
            tmp_str += j
    return tmp_str.lower()
main()