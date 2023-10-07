def say_Adieu():
    tmp_list = []
    final_string = "Adieu, adieu, to "
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            break
        else:
            tmp_list.append(name)

    if len(tmp_list) == 1:
        print(final_string + tmp_list[0])
    elif len(tmp_list) == 2:
        print(final_string + tmp_list[0] + " and " + tmp_list[1])
    else:
        print(final_string + ", ".join(tmp_list[:-1]) + ", and " + tmp_list[-1])


say_Adieu()
