"""Guessing number game"""

from random import randint

number = randint(0 ,10)
print(number)
counter=0
while True:
    try:
        counter+=1
        guess = int(input("Enter a number from 1- 10 \n"))
        if 0 <= guess <= 10:
            if number == guess:
                print(f"YOU ARE WINNER ON try {counter}  ")
                break
        else:
            print("1-10")
    except ValueError:
        print("Incorrect Entry")
