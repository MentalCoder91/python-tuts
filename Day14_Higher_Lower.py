import random
from random import choice
from game_data import data

def compute_result(ch_a, ch_b, in_ans, score_data):
    if ch_a['follower_count'] > ch_b['follower_count'] and in_ans == 'A':
        score_data += 1
    elif ch_b['follower_count'] > ch_a['follower_count'] and in_ans == 'B':
        score_data += 1
    else:
        return False, score_data
    return True, score_data

def choose_a(data_a):
    random_a = random.choice(data_a)
    return random_a, random_a['name']

def choose_b(data_b):
    random_b = random.choice(data_b)
    return random_b, random_b['name']

def generate_choices(dicts, pass_data):
    if pass_data:
        choice_one = choose_a(dicts)
        choice_two = choose_b(dicts)
        if choice_one[1] == choice_two[1]:
            generate_choices(dicts, pass_data)
        else:
            return choice_one[0], choice_two[0]
    else:
        return choose_b(dicts)[0]

play = True
score = 0
first_pass = True
while play:
    if first_pass:
        choice_a, choice_b = generate_choices(data, first_pass)
    else:
        choice_b = generate_choices(data, first_pass)
    print(f"Compare A: {choice_a['name']} , a {choice_a['description']}, from {choice_a['country']} ")
    print(f"Against B: {choice_b['name']} , a {choice_b['description']}, from {choice_b['country']} ")
    answer = str(input("Who has more number of followers? A or B: "))
    print(answer)
    result, score = compute_result(choice_a, choice_b, answer, score)
    if result:
        choice_a = random.choice([choice_a,choice_b])
        first_pass = False
        print(f"Your score is now: {score}")
    else:
        print(f"Sorry that's wrong final score is :{score}")
        break
