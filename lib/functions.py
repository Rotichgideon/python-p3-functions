#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    result = num1 + num2
    print (result)
    return result
    print(result)

def halve(number):
    result ="null" if not isinstance(number, (int, float)) else number /2
    print (result)
    return result


    greet_programmer()
    greet("Naureen")
    greet_with_default()
    greet_with_default("Naureen")
    add(3,2)
    halve("j")
