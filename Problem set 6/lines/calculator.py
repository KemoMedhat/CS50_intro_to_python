


def main():
    x = input()
    print(square(x))

# import csv
# name = input("name: ")
# home = input("home: ")
# age = input("age: ")
# with open("students.csv","a") as file :
#     writer = csv.writer(file)
#     writer.writerow([name, home, age])

def square(n):
    return n * n

if __name__=="__main__":
    main()