class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if (self.cookies + n) <= self.capacity:
            self.cookies += n
        else:
            raise ValueError("more than jar Capacity")

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Withdraw error")
        self.cookies -= n

    @property
    def capacity(self):
        return 12

    @property
    def size(self):
        return self.cookies

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError


# def main():
#     jar = Jar()
#     jar.deposit(8)
#     print(jar.size)
#     jar.withdraw(3)
#     print(jar.size)
#     jar.withdraw(58)


# if __name__ == "__main__":
#     main()
