# Initial Testing
 
Python Validator:
ADD SS HERE

# Website Testing (Solving Issues):

The first issue I encountered is that I have validate the ticker the user enters before they can move on with the porgram. This is because if an invalid ticker is entered there will be no output as the API cannot be called. In order to do this, I have to check that the ticker they entered matches with a ticker present on CoinMarketCap, however this is where the issue lies. I was unable to simply pass in the variable which holds the users input into the API call as it would return an error. 

Therefore, I decided that I would need to collect all the available tickers taken from my params (coinmarketcap.py line 9) and push them to a list. This list can then be iterated through against the users input where I can then validate whether their input is valid or not. As a result, I created a new function called get_ticker_list() that would do just this.   

```
tickerList = []

def get_ticker_list():
    for d in data['data']:
        ticker = d['symbol']
        tickerList.append(ticker)

```

tickerList[] is the list which will hold all the ticker in my params range. The function is simple, it iterates through data which holds the json file of all the latest listings. A variable 'ticker' is then created which stores each symbol within the API. Finally, tickerList is then appended to creating the list of tickers I can validate from. By printing out tickerList you can see the first 250 coins from CoinMarketCap.

![tickerList](assets/images/testing/tickerlist.png)

The next step was to create the validate_ticker(ticker) function which would iterate through tickerList and check to see if the users input exists within the list.

```
def validate_ticker(ticker):
    """
    Will validate if the users ticker exits in tickerList
    """
    for x in tickerList:
        if ticker in tickerList:
            print(f"{ticker} exists in CoinMarketCap")
            return True
            break
        else:
            print(f"{ticker} does not exist in CoinMarketCap")
            return False
            break

```

get_ticker_list() takes in ticker (which is the user input) as a parameter. It iterates through tickerList and checks to see if ticker is an element within the list. If it is, it returns True and a print statement saying that it valid, else it returns False. This was I can use the returned value as a flag to ask the user to either enter a new ticker or allow them to move on with the program. 

![validateTicker](assets/images/testing/validateticker.png)

```
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
```

This function is responsible for handling the user input and is where the validate_ticker(ticker) is called. It handles the input by asking for the ticker the user would like to know about. If 'ticker' (line 61) is empty then the appropriate output is displayed. Additionally, if the input is less than 3 characters a message will output as all tickers have 3 character minimum and would therefore be a void input. If it does meet these conditions then it asks the user to confirm their input and will ouput the neccessary response. If the response is 'y' then 'ticker' will then be passed to validate_ticker(ticker) to see if their input exists within the list.

Below is an example of a valid input:

![ValidInput](assets/images/testing/validinput.png)

Below is an example of another valid input but where the user decided to change the ticker they would like research:

![ValidInput2](assets/images/testing/validinput2.png)

Here is shows what outputs when the users inputs are invalid:

![ValidInput3](assets/images/testing/validinput3.png)