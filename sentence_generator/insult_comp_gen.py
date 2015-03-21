import random

def Insultlist():
    list1 = ['grumpily', 'bitterly', 'arrogantly', 'foolishly', 'heartlessly', 'monstrously', 'nastily', ' obnoxiously', 'redundantly']
    list2 = ['ignorant', 'lousy', 'stubborn', 'slimy', 'arrogant', 'rusty', 'careless', 'vile', 'dirty', 'crude', 'poor', 'fat', 'ugly', 'stupid']
    list3 = ['rat', 'husky', 'brat', 'loser', 'airhead', 'chicken', 'pirate']
    list1code= list1[random.randint(0,8)]
    list2code= list2[random.randint(0,7)]
    list3code= list3[random.randint(0,6)]
    string= "You are a " + list1code + " " + list2code + " " + list3code
    return string

def ComplimentList():
    list1= ['beautifully', 'cheerfully', 'fantastically', 'devotedly', 'happily', 'gleefully', 'gratefully', 'magically', 'perfectly']
    list2= ['courteous', 'amiable', 'compassionate', 'charming', 'energetic','gentle', 'patient', 'reliable', 'sympathetic','thoughtful']
    list3= ['person', 'individual', 'unicorn', 'fellow', 'bro', 'dude']
    list1code= list1[random.randint(0,8)]
    list2code= list2[random.randint(0,9)]
    list3code= list3[random.randint(0,5)]
    string="You are a " + list1code + " " + list2code + " " + list3code
    return string




c = raw_input( '\nDo you want a Compliment or an Insult? Type c for compliment or i for insult or r for random or s to stop the program \n')
while c != 's':
    if c== 'i':
        print Insultlist()
    elif c== 'c':
        print ComplimentList()
    elif c== 'r':
        rand= random.randint(0,1)
        if rand == 1:
            print Insultlist()
        else:
            print ComplimentList()
    else:
        print "\nThat is not a command. Please enter c, i, r, or s."
    c = raw_input('\nDo you want a Compliment or an Insult? Type c for compliment or i for insult or s to stop the program \n')