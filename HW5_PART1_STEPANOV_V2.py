#HW5_PART1_STEPANOV VERSION 2
def firstside():
    print("+", 5*'-', '+')


def secondside():
    for x in range(2):
        print('|', 5*' ', '|')

def total():
    firstside()
    secondside()
    firstside()



total()