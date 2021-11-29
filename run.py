# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
import sys
from programfiles.setup import title_screen

title_screen()


def clear_terminal():
    """
    When called will clear the terminal
    """
    os.system('clear')

