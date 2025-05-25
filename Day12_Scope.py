import Day12_constants as const

enemies = 1
print(const.PI)
global_var = 10


# Avoid modifying global vars in local scope
def increase_enemies():
    global enemies
    enemies += 1
    print(f"Global var: {global_var}")
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# If statements:  defined a variable then accessible locally(No block scope like in Java if/else)
if 3 > 2:
    anish = "Anish"

print(anish)
