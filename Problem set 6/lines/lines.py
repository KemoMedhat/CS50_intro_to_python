import sys
not_a_code_lines = 0
try:
    if 1 < len(sys.argv) > 2:
        sys.exit("Too few/many command-line arguments")
    elif(".py" not in sys.argv[1]):
        sys.exit("Not a Python file")
except (FileNotFoundError):
    sys.exit("File does not exist")
else:
    with open(sys.argv[1]) as file:
        reader = file.readlines()
        for line in reader:
            if (line.strip().startswith("#") or line.isspace()):
                not_a_code_lines +=1

    print(len(reader)-not_a_code_lines,end="")



    print(tabulate(table, headers, tablefmt="grid"))
