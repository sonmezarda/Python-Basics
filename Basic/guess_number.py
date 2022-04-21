import random
random_number = random.randint(0,100)
print("If you want to exit the game enter -1")

while True:
    entered_number = input("Enter the number: ")
    if entered_number == '-1':
        break
    else:
        entered_number = int(entered_number)
        if entered_number < random_number:
            print("Your number is too low")
        elif entered_number > random_number:
            print("Your number is too high")
        elif entered_number == random_number:
            print("Congrats!! You won!!")
            break