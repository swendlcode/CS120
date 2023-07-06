myfavoritefood = ['hotdog', 'pizza', 'cake', 'apples', 'noodles']
for i in range(4):
    yourfood = input('What is your favorite food: ')
    if myfavoritefood[0] == yourfood.lower():
        print('I love', myfavoritefood[0] ,'too')
    elif myfavoritefood[1] == yourfood.lower():
        print('I love', myfavoritefood[1] ,'too')

    elif myfavoritefood[2] == yourfood.lower():
        print('I love', myfavoritefood[2] ,'too')

    elif myfavoritefood[3] == yourfood.lower():
        print('I love', myfavoritefood[3] ,'too')

    elif myfavoritefood[4] == yourfood.lower():
        print('I love', myfavoritefood[4] ,'too')
    else:
        print('I dont care about much about', yourfood,'either.')

