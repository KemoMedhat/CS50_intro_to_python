month = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}


def bring_the_date(text):
    while True:
        try:
            date = input(text).strip()
            if "/" in date:
                date_as_list = date.split("/")
                tmp_list = []
                for i in date_as_list:
                    if len(i) == 1:
                        tmp_list.append("0{}".format(i))
                    else:
                        tmp_list.append(i)
                if int(tmp_list[0]) <= 12 and int(tmp_list[1]) <= 31:
                    print("{0[2]}-{0[0]}-{0[1]}".format(tmp_list))
                    break
                else:
                    raise Exception("")
            elif "," in date:
                date_as_string = date.split(" ")
                if date_as_string[0] in month.keys():
                    Y = date_as_string[2]
                    M = month[date_as_string[0]]
                    tmp_day = date_as_string[1].replace(",", "")
                    if len(tmp_day) == 1:
                        D = "0" + tmp_day[0]
                    elif len(tmp_day) == 2:
                        if int(tmp_day) <= 31:
                            D = tmp_day[0:2]
                    else:
                        raise Exception("")
                    print(f"{Y}-{M}-{D}")
                    break
            else:
                raise Exception("")

        except (Exception, ValueError):
            pass


def main():
    bring_the_date("Date: ")


main()
