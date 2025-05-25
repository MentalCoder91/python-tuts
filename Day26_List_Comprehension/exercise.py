
with open('file1.txt', 'r') as file1:
    list1 = [int(n) for n in file1.readlines()]

with open('file2.txt', 'r') as file2:
    list2 = [int(n) for n in file2.readlines()]

print(list1)
print(list2)

def check_in_list2(num):
    if num in list2:
        return True
    else:
        return False

list_common = []
for k in list1:
    if check_in_list2(k):
        list_common.append(k)

print(list_common)




