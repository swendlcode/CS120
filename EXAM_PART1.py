#BMI(Body Mass Index)

yourmass = float(input('Your mass (lbs): '))
yourhight = float(input('Your height (inches): '))
bmi = round((yourmass/(yourhight*yourhight)) *703, 2)
print('Your BMI is', bmi)
if bmi < 18.5:
    print('Underweight')
elif (bmi > 18.5) and (bmi <= 25):
    print('Normal')
elif bmi > 25:
    print('Overweight')
