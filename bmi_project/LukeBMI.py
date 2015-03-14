print('\t\t\tBMI Calculator')
print('\t\t\tBy The Late Bloomerz')
print('\nHi, this is The LB-BMI Calculator!')

print('Please use imperial units: ')


height = int(input('Please enter your height input in inches(whole number): ')) * .025
weight = int(input('Please enter your weight input pounds(whole number): '))
bmi = (weight*.45)/(height*height)

if bmi <= 18.5:
    print('Your BMI is' + str(bmi) + ' which means you are underweight... >;3')

elif bmi > 18.5 and bmi <= 25:
    print('Your BMI is'+ str(bmi) + ' which means you are normal. NICE ;D')

elif bmi > 25 and bmi <= 30:
    print('Your BMI is'+ str(bmi) + ' which means you are OVERWEIGHT!!! GO FOR A RUN AND STAY AWAY FROM SUGAR. :D')

elif bmi > 30:
    print('Your BMI is'+ str(bmi) + ' which means you are OBESE!!! GO SEE A DOCTOR.')

