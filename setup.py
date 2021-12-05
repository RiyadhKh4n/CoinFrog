import time
import sys
# import os
from coinmarketcap import *


def clear_terminal():
    """
    When called will clear the terminal
    """
    os.system('clear')


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
            clear_terminal()
            display_info()
            break

        elif screen_choice == '2':
            clear_terminal()
            get_coin_data()
            break

        elif screen_choice == '3':
            clear_terminal()
            convert_page()
            break

        elif screen_choice == '4':
            clear_terminal()
            main_menu()
            break

        else:
            print(f"> {screen_choice} is an Invalid Choice. Please type '1', '2', '3' or '4'")


def display_info():
    """
    Outputs what the program is about and how to use each function
    """
    time.sleep(1)
    print("||----------------------------------------------------------------------||")
    typewriter(MESSAGE)
    print("||----------------------------------------------------------------------||")

    main_menu()
  

MESSAGE = "CoinFrog aims to make cryptocurrency research that little bit easier\n\
                    It has two main functions:\n\
\nThe first function allows the user to retrieve all types of live coin data \n\
Simply enter the coins ticker (e.g BTC) and a brief description of the coin will appear\n\
Additionally, you can chose data that you would like to see and the program will output it\n\
\nThe second being a cryptocurrency converter function ~\n\
Simply chose between Convert FIAT or Convert CRYPTO\n\
\nIf FIAT: Enter the amount of $dollars available\n\
         Enter the ticker of the coin to buy\n\
         And CoinFrog will calc how many coins you can purchase\n\
\nIf CRYPTO: Enter the ticker of the coin to buy\n\
           Enter amount of coins you wish to purchase\n\
           And CoinFrog will calculate how much $dollars in needed\n"            

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

        ticker_length = 0
        for x in ticker:
            ticker_length = ticker_length + 1

        if ticker_length == 0:
            time.sleep(0.5)
            print("Ticker cannot be blank!")
            print("----------------------------------------------------------")

        elif ticker_length < 2:
            time.sleep(0.5)
            print("Ticker must have 2 characters minimum")
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

                if true_or_false: 
                    clear_terminal()
                    time.sleep(1)
                    print("----------------------------------------------------------")
                    print("Available Data:")                   
                    print("- Price: latest average trade price across markets")
                    print("- Volume_24h: rolling 24 hour adjusted trading volume")
                    print("- Volume_change_24h: rolling 24 hour adjusted trading volume")
                    print("- Percent_change_1h: 1 hour trading price percentage change for each currency")
                    print("- Percent_change_24h: 24 hour trading price percentage change for each currency")
                    print("- Percent_change_7d: 7 day trading price percentage change for each currency")
                    print("- Market_cap: Crypto market capitalization is the total value of a cryptocurrency")  
                    print("- Market_cap_dominance: Dominance is a measure of how much of the total market cap of crypto is comprised of the coin")
                    print("- Fully_diluted_market_cap: total value of the coin at today's price if the entire supply of coins were in circulation")
                    print("----------------------------------------------------------")
                    
                    time.sleep(2)
                    data_to_view = prompt_toolkit_function()
                    
                    time.sleep(1)
                    display_coin_data(ticker, data_to_view)

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

    print("""

          Would you like to:
      -  (1) Convert FIAT   -
      -  (2) Convert CRYPTO -  

      ENTER '1' or '2'\n""")

    true_or_false = False
    amount_validated = False
    screen_choice = ''

    while screen_choice not in ['1', '2']:
        screen_choice = input('     > ').strip()

        if screen_choice == '1':
            while amount_validated is False:
                print("-------------------------------------")
                time.sleep(1)
                print("Enter dollar amount available: ")
                usd_amount = input('> $').strip()
                amount_validated = validate_amount(usd_amount)

                if amount_validated:
                    amount_validated = True
                    time.sleep(1)

            while true_or_false is False:
                print("-------------------------------------")
                time.sleep(1)
                print("Enter ticker of coin to purchase: ")
                ticker = input('> $').upper()

                ticker_length = 0
                for x in ticker:
                    ticker_length = ticker_length + 1

                if ticker_length == 0:
                    time.sleep(1)
                    print("Ticker cannot be blank!")

                elif ticker_length < 2:
                    time.sleep(1)
                    print("Ticker must have 2 characters minimum")

                else:
                    true_or_false = validate_ticker(ticker)

                    if true_or_false:
                        true_or_false = True
                        print(f"You have ${usd_amount} available and you want to buy {ticker}")
                        print("-------------------------------------")
                        time.sleep(1)
                        calculate_coin_amount(usd_amount, ticker)
                        time.sleep(1)

        elif screen_choice == '2':
            while true_or_false is False:
                print("-------------------------------------")
                time.sleep(1)
                print("Enter ticker of coin to purchase: ")
                ticker = input('> $').upper()

                ticker_length = 0
                for x in ticker:
                    ticker_length = ticker_length + 1

                if ticker_length == 0:
                    time.sleep(1)
                    print("Ticker cannot be blank!")

                elif ticker_length < 2:
                    time.sleep(1)
                    print("Ticker must have 2 characters minimum")

                else:
                    true_or_false = validate_ticker(ticker)

                    if true_or_false:
                        true_or_false = True
                        time.sleep(1)
           
            while amount_validated is False:
                print("-------------------------------------")
                time.sleep(1)
                print("Enter amount of coins to buy: ")
                amount = input('> ').strip()
                amount_validated = validate_amount(amount)

                if amount_validated:
                    amount_validated = True
                    print(f"You want to buy {amount} ${ticker}")
                    print("-------------------------------------")
                    time.sleep(1)
                    calculate_usd_amount(amount, ticker)
                    time.sleep(1)

        else:
            print(f"{screen_choice} is an Invalid option")