import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

df = pd.read_csv('nato_phonetic_alphabet.csv', sep=',')
print(df)

data_dict = {row.letter: row.code for (index, row) in df.iterrows()}

print(data_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


#My horrible solution

# is_game = True
# output = []
# while is_game:
#     word = str(input('Enter the word: ')).upper()
#     letter_list = [letter for letter in word]
#     for item in letter_list:
#         for row in data_dict.items():
#             if item == row[0]:
#                 output.append(row[1])
#     print(output)
#     output.clear

is_game = True
output = []
while is_game:
    try:
        word = str(input('Enter the word: ')).upper()
        letter_list = [data_dict[letter] for letter in word]
        print(letter_list)
        letter_list.clear()
    except Exception as e:
        print("Sorry Letters and alphabets only")
        continue


