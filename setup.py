import time
import sys
import os
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
        #######################\n""")


    print(""" 
                    ___-----___
                ...;;;--'~~~`--;;;...
              /;-~IN CRYPTO WE TRUST~-.\
            //      ,;;;;;;;;          \\
          .//      ;;;;;    \           \\
          ||       ;;;;(   /.|           ||
          ||       ;;;;;;;   _\          ||
          ||       ';;  ;;;;=            ||
          ||LIBERTY | ''\;;;;;;          ||
           \\     ,| '\  '|><| 2021    //
            \\   |     |      \  A    //
             `;.,|.    |      '\.-'   /
                ~~;;;,._|___.,-;;;~'
                    ''=--' """)

    time.sleep(5)


    main_menu()


def main_menu():
    """
    Displays the menu for the user to interact with
    """
    print("""
      -  (1) What is CoinFrog?    -
      -  (2) Get Coin Information -
      -  (3) Crypto Converter     -   

      Type '1', '2', '3'\n""")

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

        else:
            print(f"> {screen_choice} is an Invalid Choice. Please type '1', '2', '3' or '4'")


def display_info():
    """
    Outputs what the program is about and how to use each function
    """
    time.sleep(1)
    print("|-----------------------------------------------------------------------------|")
    typewriter(MESSAGE)
    print("|-----------------------------------------------------------------------------|")

    time.sleep(4)
    clear_terminal()
    main_menu()
  

MESSAGE = " CoinFrog aims to make cryptocurrency research that little bit easier\n\
                    It has two main functions:\n\
\n'Get Coin Information' allows you to retrieve all types of live coin data\n\
Enter the coins ticker (e.g. BTC) and select the data you would like to view.\n\
\nThe second being a Crypto Converter function:\n\
Chose between 'Calculate Amount of Coins', 'Calculate USD' or 'Convert Crypto':\n\
\nCalculate Amount of Coins: Enter the amount of dollars available\n\
        Enter the ticker of the coin you wish to buy\n\
        And CoinFrog will calculate how many coins you can purchase\n\
\nCalculate USD: Enter the ticker of the coin to buy\n\
        Enter amount of coins you wish to purchase\n\
        And CoinFrog will calculate how much money is needed\n\
\nConvert Crypto: Enter the amount and ticker a coin (e.g. 5 $BTC)\n\
        along with the coin you would like to convert it into (e.g. ETH)\n\
        and CoinFrog will calculate the conversion between the two\n"            

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
                    exit_data = False

                    while exit_data is False:
                        time.sleep(1)
                        print("Available Data:")                   
                        print("- price: latest average trade price across markets")
                        print("- volume_24h: rolling 24 hour adjusted trading volume")
                        print("- volume_change_24h: rolling 24 hour adjusted trading volume")
                        print("- percent_change_1h: 1 hour trading price percentage change for each currency")
                        print("- percent_change_24h: 24 hour trading price percentage change for each currency")
                        print("- percent_change_7d: 7 day trading price percentage change for each currency")
                        print("- market_cap: market cap is the total value of a cryptocurrency")  
                        print("- market_cap_dominance: Measure of how much of the total market cap of crypto is comprised of the coin")
                        print("- fully_diluted_market_cap: value of the coin at today's price if the entire supply of coins were in circulation")
                        print("Enter 'quit' to be redirected to the Main Menu")
                        print("--------------------------------------------------------------")
                        
                        time.sleep(2)
                        data_to_view = prompt_toolkit_function()
                
                        if ((data_to_view == "quit") or (data_to_view == "QUIT") or (data_to_view == "exit") or (data_to_view == "EXIT")):
                            exit_data = True
                            clear_terminal()
                            main_menu()

                        else:
                            time.sleep(1)
                            display_coin_data(ticker, data_to_view)
                            print("----------------------------------------------------------")

                else:
                    time.sleep(0.5)
                    print("Please try again...")
                    print("----------------------------------------------------------")

            elif choice == ("n"):
                print("Nevermind, try again...")
                time.sleep(0.5)

            elif choice == ('EXIT' or 'exit' or 'quit' or 'QUIT'):
                print("Taking you to Main Menu...")
                time.sleep(2)
                print("----------------------------------------------------------")
                clear_terminal()
                main_menu()

            else:
                time.sleep(0.5)
                print(f"{choice} is an invalid option")


def convert_page():
    """
    Function which handles the crypto conversion feature
    """

    print("""

          Select An Option:
      -  (1) Calculate Amount of Coins  -
      -  (2) Calculate USD needed       -
      -  (3) Convert Crypto             -  
      -  (4) Exit to Main Menu          -

      ENTER '1' / '2' / '3' / '4'\n""")

    true_or_false = False
    true_or_false1 = False
    amount_validated = False
    screen_choice = ''

    while screen_choice not in ['1', '2', '3', 'exit', 'quit', 'QUIT', 'EXIT']:
        screen_choice = input('     > ').strip()

        if screen_choice == '1':
            clear_terminal()
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
                        print(f"Balance: ${usd_amount}")
                        print(f"Token: ${ticker}")
                        print("-------------------------------------")
                        time.sleep(1)
                        calculate_coin_amount(usd_amount, ticker)
                        time.sleep(2)
                        print("-------------------------------------")
                        print("Redirecting you to Convert Page...")
                        time.sleep(3)
                        clear_terminal()
                        convert_page()

        elif screen_choice == '2':
            clear_terminal()
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
                time.sleep(1)
                print("Enter amount of coins to buy: ")
                amount = input('> ').strip()
                amount_validated = validate_amount(amount)

                if amount_validated:
                    amount_validated = True
                    time.sleep(2)
                    print("-------------------------------------")
                    print(f"Amount to Purchase: {amount}")
                    print(f"Token Of Interest: {ticker}")
                    time.sleep(2)
                    print("-------------------------------------")
                    calculate_usd_amount(amount, ticker)
                    print("-------------------------------------")
                    time.sleep(1)
                    print("Redirecting you to Convert Page...")
                    time.sleep(3)
                    clear_terminal()
                    convert_page()

        elif screen_choice == '3':
            clear_terminal()
            while amount_validated is False:
                print("-------------------------------------")
                time.sleep(1)
                print("Enter Amount to Convert: ")
                amount = input('> ').strip()
                amount_validated = validate_amount(amount)

                if amount_validated:
                    amount_validated = True
                    time.sleep(1)

                    while true_or_false is False:
                        print("-------------------------------------")
                        time.sleep(1)
                        print("Enter Ticker: ")
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

                            if true_or_false is True:
                                true_or_false = True
                                print(f"Data so far {amount} ${ticker} -->")
                                time.sleep(1)

                                while true_or_false1 is False:
                                    print("-------------------------------------")
                                    time.sleep(1)
                                    print(f"Enter Coin to Convert {amount} ${ticker} into: ")
                                    ticker1 = input('> $').upper()

                                    ticker_length = 0
                                    for x in ticker1:
                                        ticker_length = ticker_length + 1

                                    if ticker_length == 0:
                                        time.sleep(1)
                                        print("Ticker cannot be blank!")

                                    elif ticker_length < 2:
                                        time.sleep(1)
                                        print("Ticker must have 2 characters minimum")
                                    
                                    else:
                                        true_or_false = validate_ticker(ticker1)

                                        if true_or_false:
                                            true_or_false1 = True
                                            print(f"{amount} ${ticker} --> {ticker1}")
                                            print("-------------------------------------")
                                            time.sleep(1)
                                            convert_two_cryptos(amount, ticker, ticker1)
                                            print("-------------------------------------")
                                            time.sleep(2)
                                            print("Redirecting you to Convert Page...")
                                            time.sleep(3)
                                            clear_terminal()
                                            convert_page()


        elif screen_choice == '4':
            time.sleep(1.5)
            print("-------------------------------------")
            print("Redirecting to Main Menu...")
            print("-------------------------------------")
            time.sleep(1.5)
            clear_terminal()
            main_menu()
    
        else:
            print(f"{screen_choice} is an Invalid option")


            #   if ticker == 'EXIT' or 'QUIT':
            #         print("-------------------------------------")
            #         print("Taking you to Main Menu...")
            #         time.sleep(2)
            #         print("-------------------------------------")
            #         clear_terminal()
            #         main_menu()
