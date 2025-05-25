# Hangman
import random


def greet():
    print("Anish")


def greet_name(name: str):
    print(name)


def greet_name_location(name: str, location: str):
    print(f"Name is {name} and location is {location}")


# greet()
# greet_name("Ruchi")
# greet_name_location("Anish", "Pune")
# greet_name_location(location = "Pune", name = "Anish")

def search_score(name, letter):
    count = 0
    for k in name:
        if k == letter:
            count += 1
    return count


def calculate_love_score(name1, name2):
    total = name1 + " " + name2
    result_1 = "true"
    result_2 = "love"
    score_1 = 0
    score_2 = 0
    for ch in result_1:
        score_1 += search_score(total.lower(), ch)
    for ch in result_2:
        score_2 += search_score(total.lower(), ch)
    print(str(score_1) + str(score_2))


calculate_love_score("Angela Yu", "Jack Bauer")
