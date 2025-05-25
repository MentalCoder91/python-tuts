numbers = [1, 2, 3, 4]

names = 'Angela'

names_list = [item for item in names]

print(names_list)

new_list = [n + 1 for n in numbers]
print(numbers)
print(new_list)


ls = [n*n for n in range(1,5) if n%2 ==0]
print(ls)
