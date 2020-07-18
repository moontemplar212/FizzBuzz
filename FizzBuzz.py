#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FizzBuzz implementation:
Count from 1 - 100. 
When the number is a multiple of 3 replace with Fizz.
When the number is a multiple of 5 replace with Buzz.
When the number is a multiple of 15 replace with FizzBuzz.
Go.
"""

def fizzBuzz():
    for i in range(0, 100, 1):
        string = ''

        if (i % 3 == 0): string += "Fizz"

        if (i % 5 == 0): string += "Buzz"

        if :
            print(f"{string}")
        else:
            print(f"{i}")

def main():
    fizzBuzz()

if __name__ == "__main__":
    main()