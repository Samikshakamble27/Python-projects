import random
number = random.randrange(1,10)
geuss= int(input("Enter the number of your choice: "))

while number!= geuss:
    if geuss> number:
        print("Enter lower number")
        geuss = int(input("Enter again: "))

    elif geuss<number:
        print("Higher number")
        geuss = int(input("Enter again: "))
    else:
        break
print("Your geuss is corect!!!")