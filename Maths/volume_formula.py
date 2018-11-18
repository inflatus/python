# rectangular prism volume = x1 * y1 * x2


def prism_volume(one, two, three):
    return one * two * three
print('Units count, so make sure they are consistent!')

side_one = float(input("x1: "))
side_two = float(input("y1: "))
side_three = float(input("x2: "))

print(prism_volume(side_one, side_two, side_three), 'cubic units')
