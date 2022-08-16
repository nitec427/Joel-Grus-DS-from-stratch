# Zip two or more lists

list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3]

# argument unpacking


def add(a, b): return a+b


try:
    print(add(*[1, 2]))
except TypeError:
    print("Add expects two inputs")

# Args and kwargs


def doubler(f):
    def g(x):
        return 2 * f(x)
    return g
