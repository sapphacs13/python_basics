hw = int(input("What was your average homework score?"))
mid = int(input("What was your score on the first Mid-Term?"))
fin = int(input("What was your score on the final exam?"))


grade = 0.40*hw+0.25*mid+0.35*fin



if grade >= 94:

    print("Your class GPA is 4.0")

elif grade >= 89:

    print("Your class GPA is 3.5")

elif grade >= 80:

    print("Your class GPA is 3.0")

elif grade >= 75:

    print("Your class GPA is 2.5")

 elif grade >= 70:

    print("Your class GPA is 2.0")

 elif grade >= 65:

    print("Your class GPA is 1.5")

 elif grade >= 60:

    print("Your class GPA is 1.0")

 elif grade < 60:

    print("Your class GPA is 0.0")
