

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + regex + " to " + regex + "$", s)
    if match:
        from_time = standardize(match.group(1), match.group(2), match.group(3))
        time = standardize(match.group(4), match.group(5), match.group(6))
        return f"{from_time} to {time}"
    else:
        raise ValueError


def standardize(hr, min, x):
    if hr == "12":
        if x == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if x == "AM":
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr)+12}"
    if min == None:
        minute = "00"
    else:
        minute = f"{int(min):02}"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()




# import re
# import sys


# def main():
#     print(convert(input("Hours: ")))


# def convert(s):
#     # try:
#     #     match1 = re.search(r"^(\d\d?):(\d\d) (A|P)M to (\d\d?):(\d\d) (A|P)M$",s)
#     #     match2 = re.search(r"^(\d\d?)(?!:\d\d?)? AM to (\d\d?)(?!:\d\d?)? PM$",s)
#     #     if match1:
#     #         H_AM = int(match1.group(1))
#     #         M_AM = int(match1.group(2))
#     #         H_PM = int(match1.group(3))
#     #         M_PM = int(match1.group(4))
#     #         if (H_AM <= 12 and M_AM < 60 and H_PM <= 12 and M_PM < 60):
#     #             value = f"{H_AM}:{M_AM} to {H_PM+12}:{M_PM}"
#     #         else :
#     #             raise ValueError()
#     #     if match2:
#     #         H_AM = int(match1.group(1))
#     #         M_AM = int(match1.group(2))
#     #         H_PM = int(match1.group(3))
#     #         M_PM = int(match1.group(4))
#     #         if (H_AM <= 12 and M_AM < 60 and H_PM <= 12 and M_PM < 60):
#     #             value = f"{H_AM}:{M_AM} to {H_PM+12}:{M_PM}"
#     #         else :
#     #             raise ValueError()
#     # except ValueError:
#     #     raise
#     # else:
#     #     return value

#     try:
#         pattern = r"^(\d\d?):?(\d\d?)? (A|P)M to (\d\d?):?(\d\d?)? (A|P)M$"
#         correct_format = re.search(pattern, s)
#         if correct_format:
#             grps = correct_format.groups()
#             if int(grps[0]) not in range(13) or int(grps[3]) not in range(13):
#                 raise ValueError()
#             if int(grps[1]) not in range(60) or int(grps[4]) not in range(60):
#                 raise ValueError()
#             f = tmp(grps[0], grps[1], grps[2])
#             l = tmp(grps[3], grps[4], grps[5])
#             return f + " to " + l
#         else:
#             raise
#     except ValueError:
#         raise


# def tmp(H, M, S):
#     if S == "P":
#         if H == "12":
#             tmp_h = 12
#         else:
#             tmp_h = int(H) + 12
#     else:
#         if H == "12":
#             tmp_h = 0
#         else:
#             tmp_h = int(H)
#     if M == None:
#         tmp_m = "00"
#         tmp_t = f"{tmp_h:02}:" + tmp_m
#     else:
#         tmp_t = f"{tmp_h:02}:" + M
#     return tmp_t


# if __name__ == "__main__":
#     main()
