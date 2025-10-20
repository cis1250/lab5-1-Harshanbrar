#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

def get_user_input():
    # Ask the user how many Fibonacci terms they want
    while True:
        print("How many sequences would you like?")
        sequences_input = input()  # user types something (comes in as a string)

        # Check if the input is a number (only digits, no letters or symbols)
        if sequences_input.isdigit():
            sequences = int(sequences_input)  # convert the string to an integer
            return sequences
        else:
            print("Please enter a positive whole number.")  # tell user it was invalid


def generate_fibonacci(sequences):
    # Case 1: User enters 0 → just print 0
    if sequences == 0:
        return [0]

    # Case 2: User enters a positive number
    elif sequences > 0:
        a, b = 0, 1  # starting values of Fibonacci sequence
        sequence = [a]

        if sequences > 1:
            sequence.append(b)

        # Loop to generate the rest of the sequence
        for i in range(2, sequences):  # start at 2 because 0 and 1 are already added
            next_term = a + b          # add the previous two numbers
            sequence.append(next_term)
            a = b                      # move b into a
            b = next_term              # move new term into b

        return sequence


def print_sequence(sequence, sequences):
    # Confirm what the user chose
    print(f"\nYou chose {sequences} sequences.")
    print("Fibonacci sequence:")
    for num in sequence:
        print(num)


# --- Program execution using the same logic as before ---
sequences = get_user_input()
sequence = generate_fibonacci(sequences)
print_sequence(sequence, sequences)
