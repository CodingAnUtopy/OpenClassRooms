# Python exercise: ZCasino
# MOOC: https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/
# URL: ./231735-tp-tous-au-zcasino


from random import randrange
from math import ceil


def welcomemsg(wallet):
    print("Welcome in ZCasino!")
    print("You have {0} in your wallet.".format(wallet))
    print()


def inputchecker(stringinput, minimum, maximum):
    # Convert numbers in string format to int format
    # Number has to be in range [minimum;maximum]
    # Function returns 0 if invalid input
    result = 0
    validinput = 0
    try:
        result = int(stringinput)
        assert minimum <= result <= maximum
        validinput = 1
        return validinput, result
    except AssertionError:
        print("Number should be in range [{0};{1}]".format(minimum, maximum))
        return validinput, result
    except ValueError:
        print("Invalid input.")
        return validinput, result


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
    # Generating a random number
    random = randrange(50)
    # Player pick a number and place a bet
    validinput = 0
    while validinput == 0:
        validinput, number = inputchecker(input("Play a number between 0 and 49: "), 0, 49)
    validinput = 0
    while validinput == 0:
        validinput, bet = inputchecker(input("Amount to bet: "), 1, wallet)  # Bet something in range [1;wallet].
    # Okay, let's see the result of the round.
    # Result is -1=lose, 0=draw, 1=win.
    # Wallet get modified based on the result of the round.
    result, wallet = getgain(wallet, bet, number, random)
    # Printing GUI
    printgui(wallet, bet, number, random, result)
    # Updating wallet
    return wallet


# Test
if __name__ == "__main__":
    playerWallet = 200  # Player have 200 in his wallet.
    roundNumber = 0  # The very first round that player play since he opened the program.
    keepPlaying = 1  # If player doesn't want to play, he should not open the game.
    welcomemsg(playerWallet)
    while playerWallet > 0 and keepPlaying == 1:  # Game continue when player has money and he want to play.
        if playerWallet > 0:  # If player has money in his wallet.
            if roundNumber > 0:
                # Ask player if he want to play another round
                # In case of ValueError, player keep playing by default.
                try:
                    keepPlaying = int(input("Keep playing? (0=no, default=yes)"))
                except ValueError:
                    print("Invalid input.")
                except AssertionError:
                    print("You did not typed 1 or 0.")
            if keepPlaying == 1:
                playerWallet = playzcasino(playerWallet)  # Play a round.
                roundNumber += 1
    if playerWallet == 0:
        print("No money, no gamble.")
    print("G-A-M-E  O-V-E-R !")
