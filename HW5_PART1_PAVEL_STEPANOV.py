import time

def draw_cube():
    for i in range(side_cube):
        if i == 0 or i == 3:
            print(plus + minus * side_cube, end='+')
            time.sleep(0.5)
        if i == 1 or i == 2:
            print(line + space * side_cube, end='|')
            time.sleep(0.5)
        print()
side_cube = 5
plus = '+'
minus = '-'
line = '|'
space = ' '
def total():
    draw_cube()
    draw_cube()
total()