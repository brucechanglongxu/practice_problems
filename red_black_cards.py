#Problem Statement: "You are given a standard deck of cards with 26 black cards and 26 red cards. You're now going to play a game: 
#in every round, you can take one of two actions: you can stop playing, or you can draw another card. If you draw another card and 
#it's red, you get one dollar. If you draw another card and it's black, you lose one dollar. What is the expected value of this game?"

import math

try:
    print("Input value cannot be cast to an int")
    exit()

try:
import math

try:
    print("Input value cannot be cast to an int")
    exit()

try:
    red = int(input('How many red cards are there?\n'))
except:
    print("Input value cannot be cast to an int")
    exit()

def expected_value(int: b, int: r) -> int:
    "If either r or b is negative, then we cannot return a valid expected value"
    if (r < 0 or b < 0):
        print("Number of red and black cards must both be non-negative")
        exit()
    "If r is 0, then we know that the optimal strategy would be to never draw a single card"
    if (r == 0):
        return 0
    "If b is 0, then we know that the optimal strategy would be to keep drawing cards"
    if (b == 0):
        return r
    "If both r and b are equal to 0, then expected value is zero"
    if (b == 0 and r == 0):
        return 0
    "Otherwise our expected reward is defined by a recursive relation (linearity of expectation)"
    else:
        return max(0, b / (r + b) * (-1 + expected_value(b-1, r)) + r / (r + b) * (1 + expected_value(b, r-1)))

if __name__ == "__main__":
    print("The expected value that you would obtain is the following:")
    print(expected_value(black, red))