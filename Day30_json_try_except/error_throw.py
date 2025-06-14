#
#
# try:
#
#     with open("data1.txt", "a") as file:
#         file.write("anish")
#
#     dict_anish = {'a':'b'}
#     print(dict_anish['a'])
#
# except FileNotFoundError:
#     file = open("data1.txt", "a")
#     file.write("anish hello")
#
# except KeyError as error_message:
#     print(f'Error with key: {error_message}')
#
# except Exception as e:
#     print(e)
#
# else:
#     print("anish alwekar") # Will get triggered if there aren't any exceptions in try block
#
# finally:
#     print("clean")
#     raise KeyError

height = float(input("Height:"))
weight = int(input("Weight:"))

if height > 3:
    raise ValueError("Human height not over 3 meters")

print(height, weight)
