import time
from programfiles.gamefunctions import *

def title_screen():
    """
    Function which gets called when game is run
    """
    time.sleep(0.5)

    print("""
    #######################
    + Welcome to CoinFrog +
    #######################""")

    time.sleep(1)

    mainMenu()
    
    

def mainMenu():
    print("""
    -   What is CoinFrog?       -
    -   Get Coin Information    -
    -   Crypto Converter        -
    -   Quit Program            -    

    Type 'info', 'data', 'convert' or 'quit'""")

    menu_selections()



def menu_selections():
    """
    The Menu the user can interact with
    """
    screen_choice = ''
    while screen_choice not in ['info', 'data', 'convert', 'quit']:
        screen_choice = input('> ').lower().strip()
        if screen_choice == 'info':
            displayInfo()
            break

        elif screen_choice == 'data':
            getCoinData()
            break

        elif screen_choice == 'convert':
            ConvertPage()
            break

        elif screen_choice == 'quit':
            mainMenu()
            break

        else:
            print("\nInvalid Choice. Please type 'info', 'data', 'convert' or 'quit'")

