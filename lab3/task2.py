import itertools
import random

def grams_to_ounces(grams):
    return grams * 28.35

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

def string_permutations(s):
    return ["".join(p) for p in itertools.permutations(s)]

def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

def has_33(nums):
    return any(nums[i] == 3 and nums[i + 1] == 3 for i in range(len(nums) - 1))

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def sphere_volume(radius):
    return (4/3) * 3.14 * radius**3

def unique_elements(lst):
    return list(dict.fromkeys(lst))

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print("*" * num)

def guess_number_game():
    name = input("What is your name? ")
    number = random.randint(1, 20)
    print(f"{name}, I am thinking of a number between 1 and 20.")
    attempts = 0
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"Good job, {name}! You guessed it in {attempts} tries!")
            break
