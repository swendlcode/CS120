#Part3
items = int(input('How many items do you want to buy: '))
if items < 10:
    print('Cost:', items*99)
elif (items >= 10) and (items <= 19):
    print('Cost:', round((items*99)-((items*99)*0.2),2), 'with discount 20%')
elif (items >=20) and (items <= 49):
    print('Cost:', round((items*99)-((items*99)*0.3),2), 'with discount 30%')
elif (items >=50) and (items <= 99):
    print('Cost:', round((items*99)-((items*99)*0.4),2), 'with discount 40%')
else:
    print('Cost:', round((items * 99) - ((items * 99) * 0.5),2), 'with discount 50%')

