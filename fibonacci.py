#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def get_user_input():
    valid = False
    while not valid:
        user_input = input("Enter the number of Fibonacci terms you want: ")
        if user_input.isdigit():
            terms = int(user_input)
            if terms > 0:
                valid = True
                return terms
            else:
                print("Please enter a positive number.")
        else:
            print("Invalid input. Please enter a whole number.")


def generate_fibonacci(n):
    sequence = []
    a = 0
    b = 1
    for i in range(n):  # using i instead of _
        sequence.append(a)
        temp = a + b
        a = b
        b = temp
    return sequence


def print_fibonacci(sequence):
    print("\nFibonacci sequence:")
    print(*sequence, sep=", ")


def main():
    num_terms = get_user_input()
    fib_sequence = generate_fibonacci(num_terms)
    print_fibonacci(fib_sequence)


main()
