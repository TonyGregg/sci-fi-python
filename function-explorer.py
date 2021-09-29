def fn1(x1, y1, z1):
    value = x1 + y1 + 2 + 20 / z1
    return value


def fn2(x1, y1=2, z1=3):
    ret_val = x1 + y1 + z1;
    return ret_val


def fn3(x, *tup):
    y = x + 5
    y = x + tup[2];
    print("Value of y is %d", y)

def fn4(x, **dic):
    y = x + 5
    y = x + dic[2];
    print("Value of y is %d", y)

if __name__ == '__main__':
    x, y, z = 1, 2, 3
    val = fn1(x, y, z)
    print("Value is ", val)

    val = fn2(5)
    print("fn2 value is ", val)
