# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Getting random letters

def rn_data(nr_ls: int, rn_ls: []) -> str:
    """Add two numbers"""
    rn = ''
    if nr_ls > len(rn_ls):
        print("Size of letters/symbols/numbers is greater than available data")
        return "Nothing"
    for n in range(0, nr_ls):
        rand_choice = random.choice(rn_ls)
        rn += rand_choice
    return rn


def rn_data_ls(nr_ls: int, rn_ls: []) -> []:
    """Add two numbers"""
    res = []
    if nr_ls > len(rn_ls):
        print("Size of letters/symbols/numbers is greater than available data")
        return "Nothing"
    for n in range(0, nr_ls):
        rand_choice = random.choice(rn_ls)
        res.append(rand_choice)
    return res


def shuffle_ls(letters_ls: [], symbols_ls: [], numbers_ls: []) -> str:
    shuffle = []
    shuffle.extend(letters_ls)
    shuffle.extend(symbols_ls)
    shuffle.extend(numbers_ls)
    random.shuffle(shuffle)
    return ''.join(shuffle)

# while True:
#     print("Welcome to the PyPassword Generator!")
#     nr_letters = int(input("How many letters would you like in your password?\n"))
#     nr_symbols = int(input(f"How many symbols would you like?\n"))
#     nr_numbers = int(input(f"How many "
#                            f"numbers would you like?\n"))
#
#     rn_lt = rn_data(nr_letters, letters)
#     rn_symbols = rn_data(nr_symbols, symbols)
#     rn_num = rn_data(nr_numbers, numbers)
#     print(f"Password is : {rn_lt}{rn_symbols}{rn_num}")


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many "
                       f"numbers would you like?\n"))

res = []
shuffled = shuffle_ls(rn_data_ls(nr_letters, letters), rn_data_ls(nr_symbols, symbols), rn_data_ls(nr_numbers, numbers))

print(f"Result shuffles is : {shuffled}")
