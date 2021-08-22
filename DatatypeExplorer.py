import re


def explore_basic_types():
    print("Inside basic type explorer")
    x = 2 + 5 * 2 + 5;
    print(x)
    x = 2 ** 8  # 2 power 8
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


def explore_strings():
    s1 = "A String in double quotes can contain 'single quote' characters"
    print(s1)
    s2 = 'A String in single quote also can contain "double quote" characters'
    print(s2)
    s3 = 'This string has ''\ tab and it ends with new line ''\nDid you get this in a new line?'
    print(s3)
    s4 = """This is triple quoted string, and the only
    String that can have real new lines        and sp      aces? ???"""
    print(s4)
    x = "Live and let  \t \tlive"
    x = x.replace("live", "enjoy")
    reg_exp = re.compile(r"[\t ]+")
    y = reg_exp.sub(" ", x)  # prints without the tab
    print("y = " + y)

    print(x)  # Live and let enjoy
    # Strings are immutable just like java
    x = x.split()
    print(x)


def explore_dictionaries():
    x = {1: "One", 2: "two"}
    print(x)
    x["first"] = "OneOne"
    print(x)
    x[("India", "China", "USA")] = ("Delhi", "Beijing", "Washington D.C")
    print(x)
    print("Keys :: ")
    print(list(x.keys()))
    print("Values")
    print(list(x.values()))

    print("x. get (1) " + x.get(1, 'Not available'))
    print("x. get ('first') " + x.get('first', 'Not available'))


if __name__ == '__main__':
    explore_basic_types()
    explore_list()
    explore_tuple()
    explore_strings()
    explore_dictionaries()
