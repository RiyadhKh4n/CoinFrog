# CoinFrog

[Link to Live Site Here](https://coin-frog.herokuapp.com/)

The purpose of CoinFrog is to allow users to gain an insight into all cryptocurrencies available on CoinMarketCap. They will be able to enter a coin they want to know more about and the programme will output the relevant information. CoinFrog also has a price converter function.

CoinFrog is a Python only programme which is run on a mock terminal. Once Run users will be navigated to the Main Menu where they can chose what they would like to do. The first option will allow them to vunderstand how the program works, providing a description of what the program is and the features it has. The second option will allow them to 'Get Coin Info' where users enter a ticker and will be able to view the coins data e.g name, price, market cap, TVL etc.  

The final option will navigate them to the 'Crypto Converter' where users will have three options. The first will ask the user to enter the USD amount they would like to spend and then the coin they would like to buy. The program will then calculate the amount of that coin they can buy with the USD available. The second option will allow the user to enter a coin and the amount they wish to buy and the program will calculate the USD needed to purchase it. The third option will allow user to convert from one cryptocurrency to another (e.g. 2 $ETH = 425 $LINK) this way they can easily calculate how much of one coin is worth in another.     

---
![AmIResponsive](documentation/readme/amiresponsive.png)
---

# User Experience (UX) 

* ## Vision
    My vision for CoinFrog is to be an application people go to if they want to quickly find out information about a certain cryptocurrency. The program is meant to be simple yet effective and provide a real use case to people intrested in crypto. Not only is the program useful if you want to find information about a coin or token but it also lets users to quickly see how much USD is needed to buy the coin of their choice. As the program also allows users to see how much of a certain coin or token they can buy with x amount of USD the program should cater for all user needs.        

* ## Aims
    To provide users an application they can go to when they want to find out more about a coin and also allow them to quickly calculate the coin or USD amount needed in order to successfully purchase the coin of their choice.

* ## Target Audience
    Crypto is for everyone so there is no specific target audience. However, the program does require you to have a basic understanding about crypto as it does ask users to enter a coin of their choice so it may not be suitable for someone who knows absolutely nothing about cryptocurrencies as they will not be able to get the most out of the program.

* ## User Stories

1. I want to easily understand the purpose of the site and learn how to use the program.

2. I want to be able to find out live cryptocurrency information

3. I want to be able to calculate the USD needed in order to purchase x amount of coins

4. I want to be able to calculate how many coins I can purchase with x amount of USD

5. I want to be able to convert x amount of one coin into another coin

6. I want to see if there are new features added to the site 

* ## Development Method 

When creating CoinFrog I will take a waterfall approach when developing. That is, creating sections of the program at a time and ensuring they work as intended before going onto the next section. I will be able to break up development by choosing small elements to work on daily, ensuring the website can be built and published in a timely fashion. As this project Python only all my time will be spent on developing and testing the logic behind the program. So I will work on developing each class and function within each class and getting them working before I move onto the next section of development. 

* ## Scope

Features to be included:

* The main title screen which will display when the user runs the program. The title screen displays the options available to the user allowing them to navigate through the program and use the different functionalities.

* The first option they can select will be the 'What is CoinFrog' section where they can learn what the program is about and the different functions of it thus allowing them to understand how the program works and what you can do with it. This is mainly for people who are not familiar with crypto as at first the program may be confusing however if you are familiar with cryptocurrencies then the program should be very simple to understand.  

* The next option they can select will be the 'Get Coin Information' section where users are able to enter a ticker of the coin they wish to know more about and a brief description will be outputted to them. As well as this, they are able to see the coins live data by selecting from the options available.

* The final option the user can select will be the 'Crypto Converter' section where users can enter the USD amount of a coin they are looking to buy and the program will calculate how much of that coin they are able to purchase with the USD available. Additionally, users can enter the amount of a certain coin they wish to purchase and the program will calculate the USD amout needed in order to purchase it. Finally, users will be able to chose a coin they would like to compare to another coin (e.g. 1 $ETH = 905 $THETA).

* ## Structure 
    
    * The mock terminal has been created for me by using the Code Institute template so all the file apart from any python files created were not made by me

    * run.py is what Heroku will run when the site is published so this is will act as my 'main' file and is responsible for running the game. Any other python files created will contain the relevant functions needed to run the game which will be imported and called in run.py 

* ## Flowcharts

* I used [LucidChart](lucidchart.com) to help design the project and create the following flowcharts.

### Program Flow Charts:

![MainFunction](documentation/flowcharts/mainfunctions.png)

Crypto Converter:

![CryptoConverter](documentation/flowcharts/cryptoconverter.png)

Get Coin Information:

![GetCoinInfo](documentation/flowcharts/getcoininfo.png)

## Design 

Landing Page:
- The page the user sees when the CoinFrog is launched
![LandingPage](documentation/readme/landingpage.png)

Main Menu:
- The menu the user uses to navigate through the program
![Menu](documentation/readme/mainmenu.png)

What is CoinFrog:
- The page the user is navigated to if they want to learn about the program
![WhatIsCoinFrog](documentation/readme/getinfo.png)

Get Coin Information:
- This is page the user is navigated to if the want to retrieve live coin data
![LiveData](documentation/readme/validate.png)


![LiveData2](documentation/readme/livedata.png)


![LiveData3](documentation/readme/error.png)


Conversion Menu ~
- The menu the user is taken to if they would like to complete a crypto conversion

![ConvertMenu](documentation/readme/convertmenu.png)

Calculate Amount of Coins:

![AmountOfCoins](documentation/readme/amountofcoins.png)

Calculate USD Needed:

![CalcUSD](documentation/readme/calcusd.png)

Calculate Crypto:

![CalcCrypto](documentation/readme/convertcrypto.png)


# Features 

Here describes the main features of the website and what the user can expect when viewing ~

## Existing Features:

The program is able 


## Future Features:


# Technologies 
## Languages Used

- [Python](https://www.python.org/)

## Frameworks, Libraries & Programs Used:

1. [GitPod](https://www.gitpod.io/):
    * GitPod was the IDE used to create the site

2. [Git](https://git-scm.com/):
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

3. [GitHub](https://github.com/):
    * GitHub is used to store the projects code after being pushed from Git. It was also used to deploy the project (GitHub Pages)

4. [Google Developer Tools](https://developer.chrome.com/docs/devtools/):
    * Used to test code throughout development

5. [Os Library](https://docs.python.org/3/library/os.html)
    * Used to clear the console.

6. [Heroku](https://dashboard.heroku.com/login)
    * Used to Deploy the Project

7. [LucidChart](https://www.lucidchart.com/pages/)
    * Used to design my flowcharts.

8. [AMiResponsive](http://ami.responsivedesign.is/)
    * To generate the image at the beginning of the README

9. [CoinMarketCap](https://coinmarketcap.com/api/)
    * Used the CoinMarketCap API to retrieve live coin data

10. [TinyPNG](https://tinypng.com/)
    * This was used to compress all images used in the README.md

11. [PEP8](http://pep8online.com/)
    * Used to validate my Python code


# Testing 

Due to the size of the testing section for CoinFrog I have created [TESTING.md](TESTING.md). It also shows all tested screenshots, any errors/bugs I encountered, and how I fixed them when creating this project. This is also where you can find any responsiveness screenshots, and browser compatibility tests.

[Link To Testing.md]()
   
# Deployment 

Deploying the project using Heroku:
* Visit the [Heroku](https://dashboard.heroku.com/login) site and create an account
* Click the "New" Button
* Click the "Create new app" button
* Provide a name for the app in the App name input field
* Select your region from the choose region dropdown menu 
* Click the "Create App" button
* Once redirected, proceed to the settings tab
* Click on the "config vars" button
* Supply a KEY of `PORT` and it's value of `8000`. The click the "add" button
* Next step is to add Buildpacks, click the "Add Buildpack" button
* The `python` buildpack needs to be added first then the `nodejs` buildpack
* Once the buildpacks have completed, go to the deploy screen, once in the deploy screen, select GitHub as the deployment method and connect your GitHub profile
* Search for the repository that you wish to deploy to Heroku and click "connect"
* Once your repository is connected to Heroku you can choose to either manually or automatically deploy your app.
* By selecting automatic deploys, Heroku will build a new version of the app each time a change has been pushed to the repository
* Manual deploys allow you to build a new version of your app whenever you click manual deploy
* If your build is successful you will then be able to visit the live site by clicking the link that is provided to you by Heroku

Command to add packages to requirements.txt, `pip3 freeze --local > requirements.txt` 

## Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/RiyadhKh4n/CoinFrog)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

    $ `git clone https://github.com/RiyadhKh4n/CoinFrog.git` 

7. Press Enter. Your local clone will be created. 

```shell
$ git clone https://github.com/RiyadhKh4n/CoinFrog.git
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/RiyadhKh4n/CoinFrog)

You will need to also install all required packages in order to run this application on Heroku, refer to [requirements.txt](requirements.txt)
* Command to install this apps requirements is `pip3 install -r requirements.txt`

# Credits 

## Content:

## Code

### Acknowledgements
* Tim - My Mentor
* Tutor Support



