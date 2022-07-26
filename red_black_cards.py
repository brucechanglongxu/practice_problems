# Problem Statement: "You are given a standard deck of cards with 26 black cards and 26 red cards. You're now going to play a game:
# in every round, you can take one of two actions: you can stop playing, or you can draw another card. If you draw another card and
# it's red, you get one dollar. If you draw another card and it's black, you lose one dollar. What is the expected value of this game?"

import math 

def expected_value(b, r) -> int:
    """
    Calculates the expected reward if our player plays the optimal strategy in this standard deck of cards 
    with the number of black and red cards taken in as parameters. The problem statement is given at the top
    of the file.

    :param 2 integer values: The number of red and black cards existing within our deck of cards
    :return: The expected reward of our player given that they play with the policy of choosing to draw
    another card with probability proportional to the ratio of remaining red and black cards
    """
    # If either r or b is negative, then we cannot return a valid expected value"
    if r < 0 or b < 0:
        print("Number of red and black cards must both be non-negative")
        return -1
    # If r is 0, then we know that the optimal strategy would be to never draw a single card"
    if r == 0:
        return 0
    # If b is 0, then we know that the optimal strategy would be to keep drawing cards"
    if b == 0:
        return r
    # If both r and b are equal to 0, then expected value is zero"
    if b == 0 and r == 0:
        return 0
    # Otherwise our expected reward is defined by a recursive relation (linearity of expectation)"
    return max(
        0,
        b / (r + b) * (-1 + expected_value(b - 1, r))
        + r / (r + b) * (1 + expected_value(b, r - 1)),
    )


if __name__ == "__main__":
    try:
        black = int(input("How many black cards are there?\n"))
        red = int(input("How many red cards are there?\n"))
        print("The expected value that you would obtain is the following:")
        print(expected_value(black, red))
    except ValueError:
        print("Input value cannot be cast to an int")
