# Functions used in the game hangman.py


from random import randrange
import os
import config
import pickle


# Function load_dictionary():
# Input : a text file with words delimited by a new line
# Output :  a list containing words in capital letters
#           only characters between A and Z are allowed
#           no special characters
def load_dictionary(path):
    try:
        with open(path, "r") as myfile:
            words = myfile.read()  # read file and put it in a string
            words_list = words.split("\n")  # split long string to word strings list
            result = []
            wordlen = config.MAXIMUM_LETTERS_PER_WORD
            for word in words_list:
                if word.isalpha() and len(word) == wordlen:  # only letters
                    result.append(word.upper())  # add words in capital letters to result list
            print("Dictionary loaded successfully. {0} word(s).".format(len(result)))
            return result
    except:
        print("Error: dictionary could not be loaded.")
        return []  # returns an empty list on error


# Function pick_a_word():
# Input : a list of words as list
# Output :  a random word in the list as string
def pick_a_word(wordslist):
    try:
        return wordslist[randrange(0, len(wordslist))]
    except:
        print("Error: could not pick a random word. APPLE is the word by default.")
        return "APPLE"


# Function load_scores():
# Input : player name
# Output : a dictionary containing scores of (string)player:(int)score
def load_scores(player):
    try:
        path = config.SCORES_PATH
        file_exist = os.path.isfile(path)
        if not file_exist:
            save_scores({player: 0})
        with open(path, "rb") as myfile:
            my_depickler = pickle.Unpickler(myfile)
            result = my_depickler.load()
            if player not in result:  # Create the key for new players and set score = 0
                print("Player {0} not found in scores.")
                result[player] = 0
            if not file_exist:
                print("New scores file has been generated.")
            else:
                print("Scores loaded successfully.")
            return result
    except:
        print("Error: could not load scores.")
        return {}


# Function save_scores():
# Input : players scores in a dictionary object type
# Output : none
def save_scores(scores_dictionary):
    try:
        path = config.SCORES_PATH
        with open(path, "wb") as myfile:
            my_pickler = pickle.Pickler(myfile)
            my_pickler.dump(scores_dictionary)
            print("Scores saved successfully.")
    except:
        print("Error: could not save scores.")


# Function  print_scores()
# Input : player name as string, players scores as dictionary
# Output : none
def welcome_msg(player, scores):
    try:
        print("Welcome {0}! Your score is {1}.".format(player, scores[player]))
    except KeyError:
        print("Player {0} not found.".format(player))
    except:
        print("Error: could not print scores.")


# Function play_a_letter()
# Input : list of played letters as list
# Output : updated list of played letters as list
# Each time a new list is created based on the input :
#   TODO - force manual destruction of input list <playedletters> each time function is called
#   TODO - returns the turns_counter : +1 if the (valid)letter is not in the mystery word
def play_a_letter(playedletters):
    if isinstance(playedletters, list):
        result = list(playedletters)
    else:
        result = []
    letter_isvalid = 0
    while letter_isvalid == 0:  # loop until a valid letter is played
        letter = input("Play a letter: ")
        letter = letter.upper()
        if letter in result:  # letter already played
            print("Letter {0} has been played already.".format(letter))
        elif len(letter) == 1 and letter.isalpha():  # letter is valid and not already played
            letter_isvalid = 1
            result.append(letter)
            print("You played the letter {0}.".format(letter))
        else:  # letter is not valid
            print("Invalid input.")
    return result


# Function print_gui()
# Input: player, scores, word_toguess, playedletters, turnscounter
# Output: none
def print_gui(player, scores, word_toguess, playedletters, turnscounter):
    print()
    print("[ Player name: {0} - Player score: {1} ]".format(player, scores[player]))
    print("[ Turn n°{0} of {1} ]".format(turnscounter, config.MAXIMUM_TURNS_PER_ROUND))
    mystery_word = "[ Word to guess: "
    for letter in word_toguess:
        if letter in playedletters:
            mystery_word += letter
        else:
            mystery_word += "*"
    mystery_word += " ]"
    print(mystery_word)
    print()


# Function inputchecker()
# Input: string
# Output: integer
# Function returns 0 by default if player did not input "1"
def inputchecker(stringinput):
    result = 0
    try:
        result = int(stringinput)
    except ValueError:
        pass
    finally:
        return result
