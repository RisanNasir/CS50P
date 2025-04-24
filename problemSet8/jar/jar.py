class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return  '🍪' * self.size

    def deposit(self, n):
        if self.capacity < n + self.size:
            raise ValueError("Invalid deposit")
        self.size = self.size + n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Invalid withdrawl")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
'''
def main():
    jar = Jar(20)
    print(jar)
    jar.deposit(15)
    print(jar)
    jar.withdraw(12)
    print(jar)
main()'''

