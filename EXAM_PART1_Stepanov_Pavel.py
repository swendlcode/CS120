import time
# True = 1 False = 0
start_time = time.time()
n = 0
while n == 0:
    age = int(input('Print your age: '))
    if 10 <= age <= 20:
        print('Young')
        n = 1
    elif 21 <= age <= 30:
        print('Student')
        n = 1
    elif 31 <= age <= 50:
        print('Professor')
        n = 1
    elif 51 <= age <= 60:
        print('Old Professor')
        n = 1
    elif 61 <= age <= 100:
        print('Retired Professor')
        n = 1
    else:
        print('ERROR')
print("--- %s seconds ---" % (time.time() - start_time))
