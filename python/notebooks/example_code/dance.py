"""
dance.py
========

Contains the infamous "boogie" function used to generate fantastic
fun at the disco.

"""

# Standard library imports
import time
import random

# Define some dance moves
moves = ["Mash Potato", "Hippy Hippy Shake", "Back flip", "Cha Cha Cha",
         "Mosh", "Slam Dive", "Waltz"]

def boogie(dance_moves):
    """
    This programme dances!
    """
    these_moves = moves + dance_moves

    for count in range(1, 5):
        print(count,)
        time.sleep(0.3)

    print("GO!")
    for i in range(50):
        time.sleep(0.3)
        index = random.randint(0, len(these_moves) - 1)
        print(these_moves[index] + ",")
