abc = input('I will help you find the discriminant! Enter arguments: A B C! (With Space): ').split()
abclist = list(map(int, abc))

d = (abclist[1]*abclist[1]) - 4*abclist[0]*abclist[2]
if d > 0:
    print('There are 2 roots.')
elif d == 0:
    print('There is only one rote.')
else:
    print(d, 'is negative. No roots.')