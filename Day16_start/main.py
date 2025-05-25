from turtle import Turtle, Screen
# from another_module import another_variable
# print(another_variable)

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "brown")
# timmy.fd(200)
# timmy.forward(200)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


table.add_column("emp_id", [101, 102])
table.add_column("emp_name", ['Anish', 'Umakant'])
table.add_column("emp_salary", [20000, 21000])

table.align = 'r'
print(table)
