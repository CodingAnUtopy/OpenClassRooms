# Python exercise: ZCasino
# MOOC: https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/
# URL: ./231735-tp-tous-au-zcasino

# To do: integer input checker + loop until valid input value

from random import randrange
from math import ceil


def printgui(wallet, bet, number, random, result):
    print("You bet", bet, "on the number", number, ".")
    print("The random number is", random, ".")
    # Printing results
    if result == -1:
        print("You lost your bet.")
    elif result == 0:
        print("You get back 50% of your bet.")
    elif result == 1:
        print("Congratulations! You won!")
    print("You have now", wallet, "in your wallet.")
    print()


def getgain(wallet, bet, number, random):
    result = -1  # -1 = lose bet, 0 = get back 50%, 1 = win 300% bet
    if number == random:
        result = 1
        return result, wallet + (2 * bet)
    elif number % 2 == random % 2:
        result = 0
        return result, wallet - bet + ceil(bet / 2)
    else:
        return result, wallet - bet


def playzcasino(wallet):
    try:
        # Generating a random number
        random = randrange(50)
        # Play a number and place a bet
        number = int(input("Play a number between 0 and 49: "))
        assert 0 <= number <= 49  # range of numbers is [minimum;maximum] = [0;49]
        bet = int(input("Amount to bet: "))
        assert 0 < bet <= wallet
        # Playing the game
        result, wallet = getgain(wallet, bet, number, random)
        # Printing GUI
        printgui(wallet, bet, number, random, result)
        # Updating wallet
        return wallet
    except AssertionError:
        print("Number not in range.")
    except:
        print("Something went wrong.")


# Test
if __name__ == "__main__":
    playerWallet = 200
    playAgain = 1
    while playerWallet > 0 and playAgain != 0:
        playerWallet = playzcasino(playerWallet)
        if playerWallet > 0:
            playAgain = int(input("Keep playing? (1=yes 0=no)"))
        else:
            print("GAME OVER! Don't gamble too much.")
