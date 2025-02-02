# Task 1: Define a class with getString and printString methods
class StringProcessor:
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input("Enter a string: ")
    
    def printString(self):
        print(self.text.upper())
        print("String printed in uppercase.")

processor = StringProcessor()
processor.getString()
processor.printString()

# Task 2: Define Shape and Square classes
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        result = self.length ** 2
        print(f"Square area: {result}")
        return result

square = Square(5)
square.area()

# Task 3: Define Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        result = self.length * self.width
        print(f"Rectangle area: {result}")
        return result

rectangle = Rectangle(5, 10)
rectangle.area()

# Task 4: Define Point class
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Point moved to: ({self.x}, {self.y})")
    
    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        print(f"Distance between points: {distance}")
        return distance

point1 = Point(0, 0)
point2 = Point(3, 4)
point1.show()
point2.show()
point1.dist(point2)

# Task 5: Define Bank Account class
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

account = Account("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)

# Task 6: Filter prime numbers from a list using filter and lambda

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 15, 3, 7, 19, 23, 31, 42]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)