#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program calculates the squares of sequential numbers starting at 0


def main():
    # this function uses a loop

    # this is to keep track of the loop and calculate the sum
    loop_counter = 1
    square = 0

    # input
    user_input_as_string = input("Enter a integer >= 0: ")

    # process & output
    try:
        user_input = int(user_input_as_string)
        if user_input >= 0:
            for loop_counter in range(user_input + 1):
                square = loop_counter * loop_counter
                print("{0}² = {1}".format(loop_counter, square))
        else:
            print("Negative integer entered, please try again.")
    except Exception:
        print("Invalid integer entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
