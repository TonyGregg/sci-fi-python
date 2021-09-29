def explore_if_else():
    x = 8
    if x > 8:
        y = 20
        z = 100
    elif x < 8:
        y = -25
        z = -125
    else:
        w = 200
        y = 0
        z = 0
        print(x, y, z, w)


def explore_for_loop():
    items = ["String", 2, 4, 6, 8, "Another string"]
    for x in items:
        if not isinstance(x, int):
            continue
        if not x % 2:
            print("found an integer dividable by 2: %d", x)


if __name__ == '__main__':
    explore_if_else()
    explore_for_loop()
