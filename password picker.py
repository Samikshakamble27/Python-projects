#it is an application which allows us to create strong password
import random
import string

print("Pick Password of your Choice")

adjective= ['rainy', 'slow', 'caring','great','own','little', 'last','new',
             'good','long','first','funny','successful','energetic' ]

noun =['apple', 'dinosaur', 'ball', 'toaster', 
         'goat', 'dragon', 'hammer', 'duck', 'panda']

number = random.randrange(50,100)

punctuations = random.choice(string.punctuation)

adjective = random.choice(adjective)
noun = random.choice(noun)

password= adjective + noun + str(number) + punctuations

print("Your Password is : %s" %password)

while True:
    adjective = random.choice(adjective)
    noun=random.choice(noun)
    number = random.randrange(50,100)
    punctuations = random.choice(punctuations)

    password = adjective + noun + str(number)+punctuations

    print("Your Password is : %s" %password)

    user_choice = input("Do you want another password? Type Y or N:")
    if user_choice == 'N':
        break
