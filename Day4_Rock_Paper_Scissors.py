import random

paper = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = [rock, paper, scissors]
computer = ['rock', 'paper', 'scissors']


user_input = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors."))
user_choice = ''
if user_input == 0:
    print('User chose rock')
    user_choice = 'rock'
    print(rock)
elif user_input ==1:
    print('User chose paper')
    user_choice = 'paper'
    print(paper)
else:
    print('User chose scissors')
    user_choice = 'scissors'
    print(scissors)


#Computer logic
computer_choice = random.choices(computer)[0]

if computer_choice == 'rock':
    print('Computer chose rock')
    print(rock)
elif computer_choice == 'paper':
    print('Computer chose paper')
    print(paper)
elif computer_choice == 'scissors':
    print('Computer chose scissors')
    print(scissors)


if user_choice == 'rock' and computer_choice == 'scissors':
    print('user wins')
elif user_choice == 'scissors' and computer_choice == 'rock':
    print('computer wins')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('user wins')
elif user_choice == 'paper' and computer_choice == 'scissors':
    print('computer wins')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('user wins')
elif user_choice == 'rock' and computer_choice == 'paper':
    print('computer wins')
else:
    print('Its a Draw')


