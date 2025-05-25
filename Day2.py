

def validate(data):
    print(type(int(data)))
    if type(int(data)) == "<class 'int'>":
        return True
    else:
        return False

print(validate("123"))

print("Your total Bill:")
bill = float(input("What is your total bill $?: \n"))
try:
    tip = float(input("What is the tip you want to enter 10 20 30?  \n"))
except:
    tip = 0
bill += bill*tip*0.01
print(f"Total bill is :{bill}")
split = input("Would you like to split the bill amount type Y/N? \n")
if split.strip() == 'Y':
    nos = float(input("How many people you want to split:?"))
    total_bill = bill / nos
    print(f"The split amount for each is ${round(total_bill,2)}")
else:
    print("Enjoy the day")







