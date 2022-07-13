""""

CS51A Assignment 4
Elly Rokeach & Hasana Parker
2/14/2022

Extra credit additions: Completed all three extra credit problems.If a letter has been previously guessed,
it will notify the player and won't add it to the guessed_letters list.
It also keeps track of how many letters the player guesses that are not in the movie.
If the user has more than 5 wrong guesses, the game ends and they recieve an alternate message.

"""

from movies import *
from random import *


def generate_underscore(movie):
    """
    Generates a list of dashes corresponding to the movie title
    :param movie: (str) title of movie
    :return: (list) list of dashes
    """

    list_of_dashes = []
    # appends either a space or a dash corresponding to the characters in the movie title to a list
    for char in movie:
        if char == " ":
            list_of_dashes.append(" ")
        else:
            list_of_dashes.append("-")
    return list_of_dashes


def list_to_string(list_of_strings):
    """
    Generates a single string with all the letters in the list capitalized
    :param list_of_strings: (list) list of strings
    :return: (str) a single string with all the letters capitalized
    """
    string = ""
    # concatenates every element in the list and a space to an empty string
    for element in list_of_strings:
        element = element.upper()
        string += element + " "
    return string[:-1]


def insert_letter(letter, list_of_strings, movie):
    """
    Replaces dashes with letter at corresponding indices of letter in title of movie
    :param letter: (str) any letter
    :param list_of_strings: (list) list of dashes
    :param movie: (str) title of movie
    :return: list of dashes partially filled in by letter in movie
    """
    indices = []
    # finds each index where the letter passed to the parameter letter is the same as the letter in movie
    # appends each index to an empty list called indices
    for i in range(len(movie)):
        if movie[i] == letter:
            indices.append(i)
    # changes the list of dashes at each index to be the letter
    for index in indices:
        list_of_strings[index] = letter
    return list_of_strings


def play_hangman():
    """
    Guess the title of a movie based on its year and description
    :return: title of movie and stats about right and wrong guesses
    """
    movies = get_movies()
    (title, description, year) = choice(movies)


    # game heading and movie hint
    print("*** Movie Hangman ***")
    print("Year: " + str(year))
    print(description)

    list_of_strings = generate_underscore(title)
    guessed_letters = []
    guesses = 0
    wrong_guesses = 0

    # iterates each time there is still a dash in list of dashes; breaks once player completes movie title or has more
    # than 5 wrong guesses.
    while "-" in list_of_strings and wrong_guesses < 5:
        # prompt user for input
        letter = input("Guess a letter: ")
        letter = letter.lower()

        # check if letter is in movie title, and if not, increase wrong guesses number
        if letter not in title:
            wrong_guesses += 1

        # check if letter is in guessed letters list, and if not, add it
        # if it is, say letter was already guessed
        if letter not in guessed_letters:
            guessed_letters.append(letter)
        else:
            print("You already guessed this letter!")
        print("Guessed letters: " + list_to_string(guessed_letters))

        updated_list = insert_letter(letter, list_of_strings, title)
        print("Movie: " + list_to_string(updated_list))
        guesses += 1

        # Displays to the user the amount of wrong guesses remaining
        print("Remaining wrong guesses " + str(5 - wrong_guesses))

    if wrong_guesses == 5:
        print("You are out of guesses!")
        print("you  lost :(")

    else:
        # print out information after finishing game
        print("You win!")
        print("The movie was: " + title)
        print("You guessed it with " + str(guesses) + " guesses")
        print("Wrong guesses: " + str(wrong_guesses))





