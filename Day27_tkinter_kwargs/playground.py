def add(*args):
    print(type(args))
    print(args[0])
    sum = 0
    for k in args:
        sum += k
    return sum


print(add(1, 2, 3, 4, 5))


# passing a dictionary to a method
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    for k, v in kwargs.items():
        print(f"{k} => {v}")
    return n


print(calculate(3, add=3, multiply=3))  # k,v
