#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Wed/Jun2/2021
# this program generates 10 random numbers between 1 and 100
# display the smallest number


import random


def smallest_random_number(smallest_number):
    # this function get the smallest number in list
    smallest = smallest_number[0]

    for counter in smallest_number:
        if counter < smallest:
            smallest = counter
    return smallest


def main():
    # this function uses an list
    random_number = []
    # start
    print("Starting ...")
    print("\nHere is a list of random numbers:")
    # input
    for loop_counter in range(0, 10):
        random_ = random.randint(1, 100)
        random_number.append(random_)
        # output
        print(
            "\nThe random number {0} is: {1}"
            .format(loop_counter + 1, random_number[loop_counter]), end="")
    # output
    print(
        "\n\nThe smallest number is {0}"
        .format(smallest_random_number(random_number)))
    print("\nDone.")


if __name__ == "__main__":
    main()
