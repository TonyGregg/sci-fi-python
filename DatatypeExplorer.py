def explore_basic_types():
    print("Inside basic type explorer")
    x = 2 + 5 * 2 + 5;
    print(x)
    x = 2 ** 8 # 2 power 8
    print(x)
    y = 1000005 ** 3
    print(y)


def explore_list():
    print("Inside list explorer")
    x = [0, 1, 2, 3, 4]
    print(x[2:])
    print(x[1:-2])
    x[1:2] = ["one", "two", 3.5]
    print(x)
    x.reverse()
    print("x reversed")
    print(x)
    print("###  end of list exploration")


def explore_tuple():
    print("Inside tuple explorer")
    x = (2, 5, "one")
    # Tuple once assigned cannot be changed
    print(x)
    # x[2] = ("another string", 2.52) TypeError: 'tuple' object does not support item assignment
    # tuple can be converted easily to list
    y = list(x)
    print(y)
    # and vice-versa
    z = tuple(y)
    print(z)


if __name__ == '__main__':
    explore_basic_types()
    explore_list()
    explore_tuple()
