import time
import sys
import os
from coinmarketcap import *


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

    main_menu()


def main_menu():
    """
    Displays the menu for the user to interact with
    """
    print("""
      -  (1) What is CoinFrog?    -
      -  (2) Get Coin Information -
      -  (3) Crypto Converter     -
      -  (4) Quit Program         -    

      Type '1', '2', '3' or '4'\n""")

    menu_selections()


def menu_selections():
    """
    The Menu the user can interact with
    """
    screen_choice = ''
    while screen_choice not in ['1', '2', '3', '4']:
        screen_choice = input('     > ').lower().strip()

        if screen_choice == '1':
            display_info()
            break

        elif screen_choice == '2':
            get_coin_data()
            break

        elif screen_choice == '3':
            convert_page()
            break

        elif screen_choice == '4':
            main_menu()
            break

        else:
            print(f"> {screen_choice} is an Invalid Choice. Please type '1', '2', '3' or '4'")


def display_info():
    """
    Outputs what the program is about and how to use each function
    """
    time.sleep(1)
    print("||---------------------------------------------------------------------------------------||")
    typewriter(message)
    print("||---------------------------------------------------------------------------------------||")

    main_menu()
  

message = "         CoinFrog aims to make cryptocurrency research that little bit easier\n\
                            It has two main functions:\n\
\nThe first function allows the user to retrieve all types of live coin data \n\
Simply enter the coins ticker (e.g BTC) and a brief description of the coin will appear\n\
Additionally, you can chose data that you would like to see and the program will output it\n\
\nThe second being a cryptocurrency converter function ~\n\
Simply chose between USD available or an Amount of coins you would like purchase\n\
Enter the ticker of the coin you are looking to buy\n\
2And CoinFrog will display the relevant information to you\n"


def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.07)

        else:
            time.sleep(1)


def get_coin_data():
    """
    Function which allows users to enter coin they wish to know more about
    and enables them to go through list of options
    """

    ticker = ''
    option = ''
    while option not in ['y', 'n']:
        true_or_false = None
        print("Enter the ticker of the coin you would like to research:")
        ticker = input('> ').upper()
        print("----------------------------------------------------------")

        tickerLength = 0
        for x in ticker:
            tickerLength = tickerLength + 1

        if tickerLength == 0:
            time.sleep(0.5)
            print("Ticker cannot be blank!")
            print("----------------------------------------------------------")

        elif tickerLength < 3:
            time.sleep(0.5)
            print("Ticker must have 3 characters minimum")
            print("----------------------------------------------------------")

        else:
            print(f"You chose {ticker} is this correct?")
            print("Enter 'Y' for Yes and 'N' for No")
            choice = input('> ').lower().strip()
            time.sleep(1)
            print("----------------------------------------------------------")
        
            if choice == ("y"):
                print("Validating Ticker...")
                time.sleep(1)
                true_or_false = validate_ticker(ticker)

                if true_or_false == True: 
                    break

                else:           
                    time.sleep(0.5)
                    print("Please try again...")
                    print("----------------------------------------------------------")

            elif choice == ("n"):
                print("Nevermind, try again...")
                time.sleep(0.5)

            else:
                time.sleep(0.5)
                print(f"{choice} is an invalid option")


def convert_page():
    """
    Function which handles the crypto conversion feature
    """
    print("hello World")
