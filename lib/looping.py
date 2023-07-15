#!/usr/bin/env python3

def happy_new_year():
    i = 0
    while i<=10:
        print(i)
        i += 1
    # code goes here!
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    square_integers = list()
    for integers in int_list:
        if isinstance(integers, int):
          square_integers.append(integers**2)
    return square_integers
    pass

def fizzbuzz():
    # code goes here!
    for i in range (1,101) :
        if i % 3 ==0 and i % 5 == 0:
            print ("FizzBuzz")
        elif i % 3 ==0:
            print ("Fizz")
        elif i % 5 ==0:
            print ("Buzz")
        else:
            print (i)

    pass
