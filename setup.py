from coinmarketcap import *
import time
import sys
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

C = "{:^80}".format


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

    print(C('#######################'))
    print(C('+ Welcome to CoinFrog +'))
    print(C('#######################\n'))

    print(C(" __~~~-----~~~~__"))
    print(C(" o...;;;--'~~~`--;;;..o"))
    print(C(" /;-~IN CRYPTO WE TRUST~-.\ "))
    print(C(" //      ,;;;;;;;;          \ "))
    print(C(".//       ;;;;;    \          \ "))
    print(C("||        ;;;;(   /.|         ||"))
    print(C(" ||        ;;;;;;;   _\        ||"))
    print(C("||        ';;  ;;;;=          ||"))
    print(C("|| RIYADH  | ''\;;;;;;        ||"))
    print(C("\      ,| '\  '|><| 2021    //"))
    print(C(" \     |     |      \  K   //"))
    print(C("`;.,|.    |      '\.-'  /"))
    print(C("~~;;;,._|___.,-;;;~'"))
    print(C("''=--'''''''"))
    time.sleep(4)
    clear_terminal()

    main_menu()


def main_menu():
    """
    Displays the menu for the user to interact with
    """
    print("\n")
    print(C(f"{Style.BRIGHT}{Fore.GREEN} CoinFrog{Fore.RESET}"))
    print(C("-  (1) What is CoinFrog?    -"))
    print(C("-  (2) Get Coin Information -"))
    print(C("-  (3) Crypto Converter     -"))
    print(C("-  (4) Exit Program         -\n"))
    print(C("Type '1', '2', '3' or '4' \n"))

    menu_selections()


def menu_selections():
    """
    The Menu the user can interact with
    """
    screen_choice = ''
    while screen_choice not in ['1', '2', '3', '4']:
        screen_choice = input('                         > ').lower().strip()

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
            print("\n\n\n\n\n\n")
            print(C(
                f"{Fore.GREEN}{Style.BRIGHT}    Thank you for using CoinFrog!"))  # noqa
            print_frog_image()
            break

        else:
            print(C(
                f">{Fore.RED} {screen_choice} is an Invalid Choice."
                " Please type '1', '2', '3' or '4'"))


def display_info():
    """
    Outputs what the program is about and how to use each function
    """
    time.sleep(1)
    print(
        "|---------------------------------------------"
        "---------------------------------|")
    typewriter(MESSAGE)
    print(
         "|---------------------------------------------------"
         "---------------------------|")

    time.sleep(5)
    print("\n")
    input(C(f"{Fore.YELLOW}{Style.BRIGHT}Press Enter to go to Main Menu{Fore.RESET}\n"))  # noqa
    time.sleep(1)
    print(C("-------------------------------------"))
    print(C(f"{Fore.GREEN}{Style.BRIGHT}Redirecting to Main Menu..."))
    print(C("-------------------------------------"))
    time.sleep(1)
    clear_terminal()
    main_menu()


MESSAGE = """
CoinFrog aims to make cryptocurrency research that little bit easier.
\nIt has two main functions:
\n'Get Coin Information' allows you to retrieve all types of live coin data.
Enter the coins ticker (e.g. BTC) and select the data you would like to view.
\nThe second being a Crypto Converter function:
Choose either 'Calculate Amount of Coins' 'Calculate USD' or 'Convert Crypto':
\nCalculate Amount of Coins: Enter the amount of dollars available
\tEnter the ticker of the coin you wish to buy
\tAnd CoinFrog will calculate how many coins you can purchase
\nCalculate USD: Enter the ticker of the coin to buy
\tEnter amount of coins you wish to purchase
\tAnd CoinFrog will calculate how much money is needed
\nConvert Crypto: Enter the amount and ticker a coin (e.g. 5 $BTC)
\talong with the coin you would like to convert it into (e.g. ETH)
\tand CoinFrog will calculate the conversion between the two\n
"""


def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.07)

        else:
            time.sleep(1)


def print_frog_image():
    print("                                 ,-.___.-.             ")
    print("                              ,-.(|)   (|),-.          ")
    print("                              \_*._ ' '_.* _/          ")
    print("                               /`-.`--' .-'\            ")
    print("                          ,--./    `---'    \,--.       ")
    print("                          \   |(  )     (  )|   /       ")
    print("                           \  | ||       || |  /        ")
    print("                            \ | /|\     /|\ | /         ")
    print("                            /  \-._     _,-/  \         ")
    print("                           //| \\  `---'  // ||\        ")
    print("                          /,-.,-.\       /,-.,-.\       ")
    print("                          o   o   o      o   o   o      ")


def get_coin_data():
    """
    Function which allows users to enter coin they wish to know more about
    and enables them to go through list of options
    """

    ticker = ''
    option = ''
    while option not in ['y', 'n']:
        true_or_false = None
        print(C(Fore.CYAN + Style.BRIGHT + "         Enter the ticker"
              " of the coin you would like to research:"))

        ticker = input('> ').upper()
        print(C("----------------------------------------------------------"))

        ticker_length = 0
        for x in ticker:
            ticker_length = ticker_length + 1

        if ticker_length == 0:
            time.sleep(0.5)
            print(C(Fore.RED + Style.BRIGHT + "Ticker cannot be blank!"))
            print(C("------------------------------"
                    "----------------------------"))

        elif ticker_length < 2:
            time.sleep(0.5)
            print(C(Fore.RED + Style.BRIGHT + "Ticker must have"
                  "2 characters minimum"))

            print(C("---------------------------------------"
                    "-------------------"))

        else:
            print(C(f"You chose {ticker} is this correct?"))
            print(C("Enter 'Y' for Yes and 'N' for No"))
            choice = input('> ').lower().strip()
            time.sleep(1)
            print(C("-------------------------------"
                    "---------------------------"))

            if choice == ("y"):
                print(C(Fore.YELLOW + Style.BRIGHT + "Validating Ticker..."))
                time.sleep(1)
                true_or_false = validate_ticker(ticker)

                if true_or_false:
                    clear_terminal()
                    exit_data = False
                    time.sleep(1)
                    clear_terminal()
                    print("Available Data:")
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}name{Fore.RESET}: "
                        " the name of the cryptocurrency")
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}circulating_supply {Fore.RESET}: approximate number of coins currently in circulation")  # noqa
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}total_supply{Fore.RESET}: approximate total amount of coins in existence right now ")  # noqa
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}max_supply{Fore.RESET}: maximum amount of coins that will ever exist")  # noqa
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}price{Fore.RESET}: latest average trade price across markets")  # noqa
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}volume_24h{Fore.RESET}:"
                        " rolling 24 hour adjusted trading volume")
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}volume_change_24h{Fore.RESET}: rolling 24 hour adjusted trading volume")  # noqa
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}percent_change_1h{Fore.RESET}: 1 hour trading price percentage change for each currency")  # noqa
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}percent_change_24h {Fore.RESET}: 24 hour trading price percentage change for each currency")  # noqa
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}percent_change_7d{Fore.RESET}: 7 day trading price percentage change for each currency")  # noqa
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}market_cap{Fore.RESET}:"
                        " Market cap is the total value of a cryptocurrency")
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}market_cap_dominance{Fore.RESET}: Measure in % how much of the total market cap is made of the coin")  # noqa
                    print(
                        f"- {Fore.CYAN}{Style.BRIGHT}fully_diluted_market_cap{Fore.RESET}: Value of coin if entire supply of coins were in circulation")  # noqa
                    print(
                        f"- Enter {Fore.RED}{Style.BRIGHT}'Quit'{Fore.RESET}"
                        " to be redirected to the Main Menu")
                    print("----------------------------------------------"
                          "----------------------------------")

                    while exit_data is False:

                        time.sleep(2)
                        data_to_view = prompt_toolkit_function()

                        if (data_to_view == "Quit"):
                            exit_data = True
                            clear_terminal()
                            main_menu()

                        if ((data_to_view == "circulating_supply") or
                                (data_to_view == "total_supply") or
                                (data_to_view == "max_supply") or
                                (data_to_view == "name")):
                            time.sleep(1)
                            display_coin_data_extra(ticker, data_to_view)
                            print(
                                "------------------------------------"
                                "--------------------------------------------")

                        else:
                            time.sleep(1)
                            display_coin_data(ticker, data_to_view)
                            print(
                                "----------------------------------"
                                "------------------------------"
                                "----------------")

                else:
                    time.sleep(0.5)
                    print(C("Please try again..."))
                    print(C("----------------------------------------"
                          "------------------"))
            elif choice == ("n"):
                print(C("Nevermind, try again..."))
                time.sleep(0.5)

            elif choice == ('EXIT' or 'exit' or 'quit' or 'QUIT'):
                time.sleep(1.5)
                print(C("-------------------------------------"))
                print(C(f"{Fore.GREEN} Redirecting to Main Menu..."))
                print(C("-------------------------------------"))
                time.sleep(2)
                clear_terminal()
                main_menu()

            else:
                time.sleep(0.5)
                print(C(f"{Fore.RED}{Style.BRIGHT}{choice} is an invalid option"))  # noqa


def convert_page():
    """
    Function which handles the crypto conversion feature
    """
    print("\n")
    print(C(f"{Style.BRIGHT}{Fore.CYAN} Select An Option{Fore.RESET}:"))
    print(C("-  (1) Calculate Amount of Coins  -"))
    print(C("-  (2) Calculate USD Needed       -"))
    print(C("-  (3) Convert Crypto             -"))
    print(C("-  (4) Exit to Main Menu          -\n"))
    print(C("ENTER '1' / '2' / '3' / '4'\n"))

    true_or_false = False
    true_or_false1 = False
    amount_validated = False
    screen_choice = ''

    while screen_choice not in ['1', '2', '3', 'exit', 'quit', 'QUIT', 'EXIT']:
        screen_choice = input('                         > ').strip()

        if screen_choice == '1':
            clear_terminal()
            while amount_validated is False:
                print(C("-------------------------------------"))
                time.sleep(1)
                print(C(Fore.CYAN + Style.BRIGHT + "    Enter "
                      "dollar amount available: "))

                usd_amount = input('> $').strip()

                amount_length = 0
                for x in usd_amount:
                    amount_length = amount_length + 1

                if amount_length == 0:
                    print(C(Fore.RED + Style.BRIGHT + "Amount "
                            "cannot be blank!"))
                    amount_validated = False

                else:
                    amount_validated = validate_amount(usd_amount)

                if amount_validated:
                    amount_validated = True
                    time.sleep(1)

            while true_or_false is False:
                print(C("-------------------------------------"))
                time.sleep(1)
                print(C(Fore.CYAN + Style.BRIGHT + "        Enter"
                      " ticker of coin to purchase: "))

                ticker = input('> $').upper()

                ticker_length = 0
                for x in ticker:
                    ticker_length = ticker_length + 1

                if ticker_length == 0:
                    time.sleep(1)
                    print(C(Fore.RED + Style.BRIGHT + "Ticker "
                            "cannot be blank!"))

                elif ticker_length < 2:
                    time.sleep(1)
                    print(C(Fore.RED + Style.BRIGHT + "Ticker must have"
                          " 2 characters minimum"))

                else:
                    true_or_false = validate_ticker(ticker)

                    if true_or_false:
                        true_or_false = True
                        print(C(f"Balance: ${usd_amount}"))
                        print(C(f"Token: ${ticker}"))
                        print(C("-------------------------------------"))
                        time.sleep(1)
                        calculate_coin_amount(usd_amount, ticker)
                        time.sleep(2)
                        print(C("-------------------------------------"))
                        input(C("Press Enter to return back"
                                " to Convert Page\n"))
                        print(C(
                            f"{Fore.YELLOW}{Style.BRIGHT}   Redirecting"
                            " you to Convert Page..."))
                        time.sleep(3)
                        clear_terminal()
                        convert_page()

        elif screen_choice == '2':
            clear_terminal()
            while true_or_false is False:
                print(C("-------------------------------------"))
                time.sleep(1)
                print(C(Fore.CYAN + Style.BRIGHT + "        Enter ticker of"
                      " coin to purchase: "))
                ticker = input('> $').upper()

                ticker_length = 0
                for x in ticker:
                    ticker_length = ticker_length + 1

                if ticker_length == 0:
                    time.sleep(1)
                    print(C(Fore.RED + Style.BRIGHT +
                            "Ticker cannot be blank!"))

                elif ticker_length < 2:
                    time.sleep(1)
                    print(C(Fore.RED + Style.BRIGHT + "       Ticker must have"
                          " 2 characters minimum"))

                else:
                    true_or_false = validate_ticker(ticker)

                    if true_or_false:
                        true_or_false = True
                        time.sleep(1)

            while amount_validated is False:
                time.sleep(1)
                print(C(Fore.CYAN + Style.BRIGHT + "    Enter amount"
                      " of coins to buy: "))
                amount = input('> ').strip()

                amount_length = 0
                for x in amount:
                    amount_length = amount_length + 1

                if amount_length == 0:
                    print(C(Fore.RED + Style.BRIGHT + "Amount cannot"
                            " be blank!"))
                    amount_validated = False

                else:
                    amount_validated = validate_amount(amount)

                if amount_validated:
                    amount_validated = True
                    time.sleep(2)
                    print(C("-------------------------------------"))
                    print(C(f"Amount to Purchase: {amount}"))
                    print(C(f"Token Of Interest: ${ticker}"))
                    time.sleep(2)
                    print(C("-------------------------------------"))
                    calculate_usd_amount(amount, ticker)
                    print(C("-------------------------------------"))
                    input(C("Press Enter to return back to Convert Page\n"))
                    time.sleep(2)
                    print(C(
                        f"{Fore.YELLOW}{Style.BRIGHT}      Redirecting"
                        " you to Convert Page..."))
                    time.sleep(3)
                    clear_terminal()
                    convert_page()

        elif screen_choice == '3':
            clear_terminal()
            while amount_validated is False:
                print(C("-------------------------------------"))
                time.sleep(1)
                print(C(Fore.CYAN + Style.BRIGHT +
                        " Enter Amount to Convert: "))
                amount = input('> ').strip()

                amount_length = 0
                for x in amount:
                    amount_length = amount_length + 1

                if amount_length == 0:
                    print(C(Fore.RED + Style.BRIGHT + "Amount cannot be blank!"))  # noqa
                    amount_validated = False
                else:
                    amount_validated = validate_amount(amount)

                if amount_validated:
                    amount_validated = True
                    time.sleep(1)

                    while true_or_false is False:
                        print(C("-------------------------------------"))
                        time.sleep(1)
                        print(C(Fore.CYAN + Style.BRIGHT + "Enter Ticker: "))
                        ticker = input('> $').upper()

                        ticker_length = 0
                        for x in ticker:
                            ticker_length = ticker_length + 1

                        if ticker_length == 0:
                            time.sleep(1)
                            print(C(Fore.RED + Style.BRIGHT + "    Ticker"
                                  " cannot be blank!"))

                        elif ticker_length < 2:
                            time.sleep(1)
                            print(C(Fore.RED + Style.BRIGHT +
                                    "       Ticker must have"
                                    " 2 characters minimum"))

                        else:
                            true_or_false = validate_ticker(ticker)

                            if true_or_false is True:
                                true_or_false = True
                                print(C(f"Data so far {amount} ${ticker} -->"))
                                time.sleep(1)

                                while true_or_false1 is False:
                                    print(C("-----------------------------"
                                          "--------"))
                                    time.sleep(1)
                                    print(C(
                                        f"{Fore.CYAN}{Style.BRIGHT}          Enter Coin to Convert {amount} ${ticker} into: "))  # noqa

                                    ticker1 = input('> $').upper()

                                    ticker_length = 0
                                    for x in ticker1:
                                        ticker_length = ticker_length + 1

                                    if ticker_length == 0:
                                        time.sleep(1)
                                        print(C(Fore.RED + Style.BRIGHT +
                                              "Ticker cannot be blank!"))
                                    elif ticker_length < 2:
                                        time.sleep(1)
                                        print(
                                            C(Fore.RED + Style.BRIGHT +
                                              "Ticker must have 2 "
                                              "characters minimum"))

                                    else:
                                        true_or_false = validate_ticker(
                                            ticker1)

                                        if true_or_false:
                                            true_or_false1 = True
                                            print(C(
                                                f"{amount} ${ticker} --> {ticker1}"))  # noqa
                                            print(C("------------------------"
                                                  "-------------"))
                                            time.sleep(1)
                                            convert_two_cryptos(
                                                amount, ticker, ticker1)
                                            print(C("-------------------------"
                                                  "------------"))

                                            input(C("Press Enter to "
                                                    "return back"
                                                    " to Convert Page\n"))

                                            time.sleep(2)
                                            print(C(
                                                f"{Fore.YELLOW}{Style.BRIGHT}"
                                                "       Redirecting you to"
                                                " Convert Page..."))

                                            time.sleep(3)
                                            clear_terminal()
                                            convert_page()

        elif screen_choice == '4':
            print("\n")
            time.sleep(1.5)
            print(C("-------------------------------------"))
            print(C(f"{Fore.GREEN}{Style.BRIGHT}Redirecting to Main Menu..."))
            print(C("-------------------------------------"))
            time.sleep(2)
            clear_terminal()
            main_menu()

        else:
            print(C(f"{Fore.RED}{screen_choice} is an Invalid option"))
