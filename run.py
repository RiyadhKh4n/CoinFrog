# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
from setup import title_screen

def clear_terminal():
    """
    When called will clear the terminal
    """
    os.system('clear')

clear_terminal()
title_screen()
