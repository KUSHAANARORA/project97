import random 

number = random.randint(1,9)

Chances = 0
while Chances < 5:
    enterednumber = int(input("enter your guess"))

    if enterednumber == number:
        print("Congratulations You Won !!!")
        break

    elif enterednumber < number:
        print("your guess was too low")

    else:
        print("your guess was too high")
    
Chances = Chances + 1



