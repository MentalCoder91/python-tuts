class User:
    name = 'Anish'
    surname = 'Alwekar'
    full_name = []

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.salary = 0
        self.follower = 0
        self.full_name.append(self.name + "->" + self.surname)

    def get_full_names(self):
        return self.full_name

    def add_follower(self):
        self.follower += 1




user_1 = User('Ruchita', 'Patil')
user_1.salary = 20000
user_2 = User('Anish', 'Alwekar')

print(user_1.salary)
user_1.add_follower()
print(user_1.follower)

print(user_2.follower)


print(user_2.get_full_names())
