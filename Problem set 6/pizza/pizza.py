import sys
import csv
from tabulate import tabulate
try:
    if 1 < len(sys.argv) > 2:
        sys.exit("Too few/many command-line arguments")
    elif(".csv" not in sys.argv[1]):
        sys.exit("Not a CVS file")
except (FileNotFoundError):
    sys.exit("File does not exist")
else:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(tabulate(reader,headers="keys",tablefmt="grid"))

