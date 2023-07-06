#Pavel Stepanov
#1 Points: 2
# What extention do programs take in Python? Is it .docx, .py, or .txt?
# Answer is: .py



#2 Points: 3
#Explain the output of following program in your own words
print("Please enter your age")
x = input( )
print("in five years you would be", int(x)+5, "years old")
#And in the next line he already sums up 5 with our age and says
#that in 5 years you will be 5 years more





#3 Points: 5
# Explain what is the error in following program. Fix the following program.
print("Please enter your age")
x = int(input())
#This program asks to keep our current age X .In the original code, X was a string (str), so it just tripled the string.
#Now we have converted to a number in integer (int) x = int(input()).
print("Someone who is three times your age would be:", x*3)
#Or we can use:
#print("Someone who is three times your age would be:", int(x) * 3)







#4 Points: 10
#Write a program that will print three names: Joe, Mary, Peter
# Then the program prints their ages as 33, 34, 44
# Finally program should print all their names, and the average age
# of the all people with one single print command
avarage = 0
print('Joe, Mary, Peter')
age = [33, 34, 44]
for i in range(len(age)):
    avarage += age[i]
avarage /= len(age)
print(age[0], age[1], age[2])
print('Joe is ' + str(age[0]) + ' years old ' +
      'Mary is ' + str(age[1]) + ' years old ' +
      'Peter is ' + str(age[2]) + ' years old. '
                                  'Their average age is ' + str((int(avarage))))




#Pavel Stepanov






