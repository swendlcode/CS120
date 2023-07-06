import time


def findDiscount(num, price):
    discount = (num * price) / 10
    return discount


start_time = time.time()

a = int(input('Item: '))
b = float(input('Price: '))
if a > 10:
    print(f'Your total price is {(a * b) - findDiscount(a, b)}$, you saved {findDiscount(a, b)}$')
elif a == 9:
    print(f'Your total price is {a * b}$, buy ONE get 10%')
else:
    print(f'Your total price is {a * b}$')
print("--- %s seconds ---" % (time.time() - start_time))
