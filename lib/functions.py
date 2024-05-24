#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2

greet_programmer()

greet("Naureen")

greet_with_default()

greet_with_default("Sunny")

sum_result = add(1, 2)

print(sum_result)

result = halve(4)
print(result)

result = halve("two")
print(result)