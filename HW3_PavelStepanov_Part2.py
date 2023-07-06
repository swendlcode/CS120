#PART 2
number = []
countnumber = 0
for a in input('Print you four number, whih space: ').split():
    number.append(int(a))
    countnumber += 1
for i in range(countnumber):
    for q in range(i+1,countnumber):
        if number[i] < number[q] or number[i] == number[q]:
            number[q],number[i] = number[i],number[q]

print('Maximum number:',number[0])
print('Minimum number:', number[countnumber - 1])

#Variable "Countnumber" simplified the program and the program runs faster than I would find out the length massive with function len(object) several times
#The program takes on many values thanks to the loop

