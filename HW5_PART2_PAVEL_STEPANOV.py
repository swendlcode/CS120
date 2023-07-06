def mainprogram(a,b,c):
    discriminant = (b ** 2 - (4 * a * c)) #Discriminant
    print(f'Descriminant is {discriminant}')
    if discriminant == 0 or discriminant < 0:
        def oneRoot(a,b):
            if discriminant == 0: #Discriminant equals 0
                singleroot = -b/(2*a)
                print(f'Descrimnant equals {discriminant}')
                print(f'Root equals {singleroot}')
        oneRoot(a, b)
        def nonRoot():
            if discriminant < 0: #Discriminant less than zero
                print(f'Descriminate less than 0 = {discriminant}')
        nonRoot()
    else:
        def plusRoot(a,b,c): #First Root Positive Version
            first_root = (-b - ((b**2 - 4*a*c)**(1/2)))/(2*a)
            print(f'Positive Version is: {first_root}')
        plusRoot(a,b,c)
        def negRoot(a,b,c): #Second Root Negative Version
            second_root = (-b + ((b**2 - 4*a*c)**(1/2)))/(2*a)
            print(f'Negative Version is: {second_root}')
        negRoot(a,b,c)

a = int(input('> '))
b = int(input('> '))
c = int(input('> '))

mainprogram(a, b, c) #Info

