# Write your code to expect a terminal of 80 characters wide and 24 rows high
from programfiles.setup import title_screen
import key 
import os
import sys

title_screen()

def clear_terminal():
    """
    When called will clear the terminal
    """
    os.system('clear')


