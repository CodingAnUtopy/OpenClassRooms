# Python exercise: hangman game
# MOOC: https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/
# URL: ./232565-tp-realisez-un-bon-vieux-pendu


import functions
import config


# Initialization
dictionary = functions.load_dictionary(config.DICTIONARY_PATH)
keep_playing = 1

while keep_playing == 1:
    turns_counter = 0
    playedletters = []
    word = functions.pick_a_word(dictionary)
    player = input("Type your name: ").upper()
    scores = functions.load_scores(player)
    functions.welcome_msg(player, scores)

    while turns_counter < config.MAXIMUM_TURNS_PER_ROUND:
        playedletters = functions.play_a_letter(playedletters)
        turns_counter += 1
        functions.print_gui(player, scores, word, playedletters, turns_counter)

    scores[player] += config.MAXIMUM_TURNS_PER_ROUND - turns_counter
    functions.save_scores(scores)
    keep_playing = functions.inputchecker(input("Keep playing? (type 1 to continue, default=stop)"))
    print()
