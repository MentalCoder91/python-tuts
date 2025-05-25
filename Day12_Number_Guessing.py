import random

random_list = [10, 32, 45, 67, 74, 83, 98]

target_num = random.choice(random_list)

def guess_result(guess_num, tgt_num):
    if guess_num > tgt_num:
        return "Too High", True
    elif guess_num < tgt_num:
        return "Too Low", True
    elif guess_num == tgt_num:
        return "You got it num is:" + str(tgt_num), False

def set_difficulty():
    user_difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard':"))
    if user_difficulty == 'easy':
        print("You have 10 attempts remaining to guess the number.")
        return 10
    else:
        print("You have 5 attempts remaining to guess the number.")
        return 5

play = True
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
attempts_g = set_difficulty()

while play:
    guess = int(input("Make a guess: "))
    res_tuple = guess_result(guess, target_num)
    if res_tuple[1]:
        print(res_tuple[0])
    else:
        print(res_tuple[0])
        play = False

    attempts_g -= 1
    print(f"Attempts remaining : {attempts_g}")
    if attempts_g == 0:
        print("You are out of attempts, You Lose!!!")
        play = False
