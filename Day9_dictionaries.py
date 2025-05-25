dict = {
    "Bug": "There is a bug",
    "Function": "There is a function",
    "Loop": "There is a Loop",

}

dict['Syntax'] = "This is a Syntax"
print(dict)

empty_dict = {}


#Edit item in dict
dict['Bug'] = "This is a new bug"

print(dict)

#Loops
#
# print(dict.keys())
# print(dict.values())
#
# print(dict['Bug'])
#
# for k, v in dict.items():
#     print(k + "->" + v)
#
# for item in dict.keys():
#     print(item)
#
# for item in dict.values():
#     print(item)

for index in dict:
    print(index)
    print(dict[index])


