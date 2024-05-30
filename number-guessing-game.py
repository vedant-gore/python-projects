import random
import math

lowerB = int(input("Enter Lower bound number -> "))
upperB = int(input("Enter Upper bound number -> "))
numberofChances = round(math.log(upperB - lowerB + 1, 2)) 
x = random.randint(lowerB, upperB)
print("\n\tYou have only ", numberofChances, "chances to guess the number!\n")
count = 0
while count < numberofChances:
    count = count + 1
    guess = int(input("Guess a number -> "))
    if x == guess:
        print("Congratulations you did it in", count, "try! :D")
        break
    elif x > guess:
        print("The number you guessed is small!")
    elif x < guess:
        print("The number you guessed is high!")
if count >= numberofChances:
    print("\nThe number is %d" %x)
    print("\nBetter luck next time! :(")