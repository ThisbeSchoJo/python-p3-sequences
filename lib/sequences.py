#!/usr/bin/env python3

def print_fibonacci(length):
    # adds current number to previous number
    # adds i to i-1
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length ==2:
        print([0, 1])
    else:
        fib_sequence = [0,1]
        for i in range(2, length):
            next_num = fib_sequence[-2]+fib_sequence[-1]
            fib_sequence.append(next_num)
        print(fib_sequence)


