# import sys
# import csv


# def main():
#     try:
#         check_agrs_number()
#         check_csv_file()
#         read_input_csv()
#     except FileNotFoundError:
#         sys.exit("File does not exist")
#     else:
#         write_output_csv(read_input_csv())


# def check_agrs_number():
#     if 1 < len(sys.argv) > 3:
#         sys.exit("Too few/many command-line arguments")


# def check_csv_file():
#     if ".csv" not in sys.argv[1]:
#         sys.exit("Not a CSV file")


# def read_input_csv():
#     names = []
#     with open(sys.argv[1]) as file:
#         reader = csv.DictReader(file)
#         for line in reader:
#             L,F= line["name"].split(",")
#             names.append(
#                 {
#                     "firts": F.strip(),
#                     "last":  L,
#                     "house": line["house"]
#                 }
#             )
#     return names


# def write_output_csv(lista):
#     with open(sys.argv[2], "w") as file:
#         writer = csv.DictWriter(file, ["first", "last", "house"])
#         writer.writeheader()
#         for row in lista:
#             writer.writerow(
#                 {"firts": row["firts"], "last": row["last"], "house": row["house"]}
#             )


# if __name__ == "__main__":
#     main()



import sys, csv

def main():
    check_arg_validity()
    scourgify()


def check_arg_validity():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def scourgify():
    try:
        input_file = open(sys.argv[1], "r")
        output_file = open(sys.argv[2], "w")

    except FileNotFoundError:
        sys.exit("Could not read file")

    column_data = csv.DictReader(input_file, delimiter=",")
    column_writer = csv.DictWriter(output_file, ["first", "last", "house"])

    column_writer.writeheader()


    for row in column_data:
        last, first = row["name"].split(",")
        column_writer.writerow({
            "first": first.strip(),
            "last": last,
            "house": row["house"]
        })

if __name__ == "__main__":
    main()