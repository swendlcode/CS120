# Heron's  formula
import time


def findTriangleArea(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
    return area


start_time = time.time()
# Main program:
a = int(input('Side A: '))
b = int(input('Side B: '))
c = int(input('Side C: '))
# My area is round two decimal place
print(f'The area of a triangle with sides of {a}, {b}, {c}. Area: {round(findTriangleArea(a, b, c), 2)}')
print("--- %s seconds ---" % (time.time() - start_time))
