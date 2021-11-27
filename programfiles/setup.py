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
    -   (1) What is CoinFrog?       -
    -   (2) Get Coin Information    -
    -   (3) Crypto Converter        -
    -   (4) Quit Program            -    

    Type '1', '2', '3' or '4'""")

    menu_selections()



def menu_selections():
    """
    The Menu the user can interact with
    """
    screen_choice = ''
    while screen_choice not in ['1', '2', '3', '4']:
        screen_choice = input('> ').lower().strip()

        if screen_choice == '1':
            displayInfo()
            break

        elif screen_choice == '2':
            getCoinData()
            break

        elif screen_choice == '3':
            ConvertPage()
            break

        elif screen_choice == '4':
            mainMenu()
            break

        else:
            print(f"> {screen_choice} is an Invalid Choice. Please type '1', '2', '3' or '4'")

