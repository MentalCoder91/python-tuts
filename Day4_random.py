import random
import my_module

#func
random_integer = random.randint(1, 10)

#0_1->floating
random_number_0_1 = random.random() * 10

#floating 1<N<=10
random_uniform = random.uniform(1, 10)

#HeadsTails

if random_integer > 5:
    print("Heads")
else:
    print("Tails")




print(random_integer)
print(random_number_0_1)
print(random_uniform)
print(my_module.my_favourite_number)
