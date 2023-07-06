#PART 1
name = input('Your name: ')

age = int(input('Your age: '))

if age < 16:
    print('Stay at home,', name)
elif age == 16 or age == 17:
    print('Yo can drive but that is all,', name)
elif age == 18 or age == 19:
    print('You can drive and vote,', name)
else:
    print('You can drive vote and gamble,', name)


