#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Various Python FizzBuzz implementations:
Count from 1 - 100. 
When the number is a multiple of 3 replace with Fizz.
When the number is a multiple of 5 replace with Buzz.
When the number is a multiple of 15 replace with FizzBuzz.
Go.
"""

#------------------------------------------------------------------------------------------------------------------------#

def fizzBuzz():
    for i in range(0, 100, 1):
        output = ''

        if not i % 3: output += "Fizz"

        if not i % 5: output += "Buzz"

        print(output or i)

#------------------------------------------------------------------------------------------------------------------------#

def getFizzBuzz(multiples, _min = 0, _max = 100, _step = 1):
    for i in range(_min, _max, _step):
        output = ''
        for j in multiples:
            if i % j == 0:
                output += multiples[j]

        if output == '': output = i

        print(f"{output}")

#------------------------------------------------------------------------------------------------------------------------#

def joinmap(func, elements, separator):
    return separator.join(map(func, elements))

def fb_value(x, fb={3:'Fizz', 5:'Buzz'}):
    words = joinmap(lambda n: fb[n] if x % n == 0 else '', fb, '')
    return words if words else str(x)

def fb_range(low=1, high=100):
    return joinmap(fb_value, range(low, 1 + high), '\n')

#------------------------------------------------------------------------------------------------------------------------#

def main():

    fizzBuzz()

    # multiples = {3: "Fizz", 5: "Buzz", 7: "Haha"} 
    # getFizzBuzz(multiples)

    # print(fb_range())

if __name__ == "__main__":
    main()