import math

def BMI(height, weight): #height in inches, weight in pounds
    w_kg = weight * .45
    h_meters = height * .025
    return 0.0 + (w_kg)/(math.pow(h_meters, 2))


def overweight(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi < 25:
        return 'normal weight'
    elif bmi < 30:
        return 'overwewight'
    else:
        return 'obese'

def input():
    name = raw_input('What is your name? ')
    weight = int(raw_input('What is your weight in pounds? '))
    height = int(raw_input('What is your height in inches? '))
    return name + ": You are " + str(overweight(BMI(height, weight)))

print input()

#testing:
#print overweight(BMI(64, 135)) #normal
#print overweight(BMI(59, 120)) #normal
#print overweight(BMI(70, 100)) #underweight
#print overweight(BMI(64, 145)) #overweight
#print overweight(BMI(50, 150)) #obese