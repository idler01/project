import math
import random

a = int(input("Enter the upper limit: "))
b = int(input("Enter the lower limit: "))

z = random.randint(b,a)
x = math.log2(a-b+1)
x = int(x)
print ("your number of guesses are: ",x)

count = 0

while count<=x:
    c = int(input("enter the number: "))
    if c<z:
        print("The guess is too low!")
    elif c>z:
        print("The guess is too high!")
    elif c==z :
        print("congratulation on winning the game!!!")
        break
    count= count+1

print("try again next time! the number was: ",z)