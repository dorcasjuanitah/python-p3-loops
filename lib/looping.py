#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        return(i -= 1)
    print("Happy New Year!")
    

def square_integers(int_list):
    squared_int_list=[int_list * 2 for int in int_list]
    return (squared_int_list)

def fizzbuzz(num):
    for num in range (100):
        return(num)

    if (num % 3):
        return("Fizz")
    elif(num % 5):
        return("Buzz")
    elif(num % 3 and num % 5):
        return ("FizzBuzz")
    else:
        return(num)
