def Personfeatures():
    person = raw_input("Enter your FULL name: ")
    for i in range(len(person)):
         if (person[i:i + 1]).isdigit():
            print("Please enter full name without any number. Try again.")
            person = raw_input("Enter you FULL name: ")
         else:
            break

    age = raw_input("Enter your age: ")
    for i in range(len(age)):
         if (not(age[i : i + 1]).isdigit()):
            print("Please enter number only.  Try again.")
            age = raw_input("Please enter your age in number only: ")
         else:
            break
         
    gender = raw_input("Enter your gender: ")
    for i in range(len(gender)):
        if (gender[i:i + 1]).isdigit():
            print ("Please enter Male or Female.  Or M for male, F for female.")
            gender = raw_input("Please enter your gender again: ")
        else:
            break
    
    weight = raw_input("Enter your weight: ")
    for i in range(len(age)):
        if (not(weight[i:i + 1]).isdigit()):
            print("Please enter number only.  Try again.")
            weight = raw_input('Please enter weight in number.  Try again: ')
        else:
            break
    
    height = raw_input("Enter your height in inches: ")
    for i in range(len(height)):
        if (not(height[i:i + 1]).isdigit()):
            print("Please enter number only.  Try again.")
            height = raw_input('Please enter height in number.  Try again: ')
        else:
            break

    return ("Your name is " + person + "Your age is " + age + "You are a " + gender + "You are " + weight + " pounds" + "You are " + height + " inches high")

print (Personfeatures())