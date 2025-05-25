# Hangman
import random


def generate_place_holder(guess_word: str) -> str:
    place_holder_len = len(guess_word)
    result = []
    for k in range(0, place_holder_len):
        result.append("_")
    return " ".join(result)


def place_in_place_holder(i: int, ltr: str, ph: str) -> str:
    ls_ph = ph.split(" ")
    ls_ph[i] = ltr
    return " ".join(ls_ph)


d_list = ["baboon", "camel"]
hang_man = random.choice(d_list)

place_holder = generate_place_holder(hang_man)
print(place_holder)
lives = 6
flag = False
idx_ls = []
while lives > 0:
    print(f"Remaining Lives : {lives}")
    guess = str(input("Enter a letter: ")).lower()
    idx = 0
    for letter in hang_man:
        if letter == guess and idx not in idx_ls:
            place_holder = place_in_place_holder(idx, letter, place_holder)
            idx_ls.append(idx)
            flag = True
            break
        else:
            flag = False
        idx += 1

    if not flag:
        lives -= 1

    print(place_holder)

    index = place_holder.find("_")
    if index != -1:
        continue
    else:
        print(f"The puzzle is solved : {hang_man} ")
        break

if "_" in place_holder:
    print("GAME OVER.. !!!!!")