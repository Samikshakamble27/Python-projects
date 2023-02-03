#FILE HANDLING = means reading from file, writing into the file and make chnages into the file
#file handling operations are read, write , delete, alter

#open mode
# r = is used to read file
f = open("financial aid application content.txt ","r")
#read mode
read_file = f.read()
print(read_file)

#write mode we use w

f = open("financial aid application content.txt ","w")
write = f.write(" Application is submitted")
#it will write in your text file
print(write)


#always remember to close file
#f.close()

'''append() 
we use append to add content at the end of the file'''

f = open("financial aid application content.txt ","a")
#new text line will get added into your txt file
append = f.write("\n application is submitted")
print(append)

#len() function is used to cout total number of characters in file

f = open("financial aid application content.txt","r")
count_char = f.read()
len = len(count_char)
print(len)

#readline() function = reads line one  by one from the text file

f = open("financial aid application content.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()



'''EXCEPTION HANDLING'''
#If the code written inside the try function having error then
#it will execute except part exception can have any number of 
#exceptions


'''as it is addition of str then it will dont do addition
of numbers concatination will happen here'''
#exception handling
a =input("enter no ")
b =input("enter no ")

#if error in try fun then except fun will execute
try:
    c = int(a)+ b
except:
    print("error in your code")


# a =input("enter no")
# b =input("enter no")
# c = a+b
# print(a+b)

a =input("enter no ")
b =input("enter no ")

#if no error in try fun then except fun will not execute
try:
    c = int(a)+ int(b)
    print(c)
except:
    print("error in your code")



#Try with Else Clause
'''if your try block is error free only then your else block will
get executed'''

a = int(input("enter the number: "))

try:
    if a%2==0:
        print("numer{a} is even")
    else:
        print("number {a}is odd")
except:
    print("error is there in try block")
else:
    print("try block is error free")



#FINALLY KEYWORD
'''finally keyword = will always execute after 
the try and except'''
a = int(input("enter the number: "))

try:
    if a%2==0:
        print("numer{a} is even")
    else:
        print("number {a}is odd")
except:
    print("error is there in try block")
else:
    print("try block is error free")
finally:
    print("finally key word will execute after try and exception block")