def Collatz(x):
    if x % 2 != 0:
        collatzfunction = 3 * x +1
    else:
        collatzfunction = x//2
    return collatzfunction

def Collataz2(x):
    result = Collatz(x)
    print(result)
    while result != 1:
        result = Collatz(result)
        print(result)

x = int(input('Your number is: '))
print(x)
Collataz2(x)