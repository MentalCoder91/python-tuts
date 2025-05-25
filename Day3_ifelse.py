print("Welcome to Pizza House")
size = input("What is your Pizza size preference bill S, M, L?: \n")
bill = 0
pepperoni = input("Do u want pepperoni on Pizza ? \n")
cheese = input("Do u want extra cheese on Pizza ? \n")

if size == 'S':
    bill = 15
    if pepperoni == 'Y' or pepperoni == 'y':
        bill += 2
elif size == 'M':
    bill = 20
    if pepperoni == 'Y' or pepperoni == 'y':
        bill += 2
elif size == 'L':
    bill = 20
    if pepperoni == 'Y' or pepperoni == 'y':
        bill += 2
else:
    print("Wrong input")

if cheese == 'Y' or cheese == 'y':
    bill += 1

print(f"Total bill of {size} Pizza is :{bill}")
