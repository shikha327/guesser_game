import random
Top_of_Number=input("Enter the number ")
if Top_of_Number.isdigit():
    Top_of_Number=int(Top_of_Number)
    if Top_of_Number<=0:
        print("Next time enter number greater than 0")
        quit()
else:
    print("Next time Enter the number! ")
    quit()

random_number=random.randint(0,Top_of_Number)
guesses=0
while True:
    guesses +=1
    user_guess=input("make a guess")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Next time Enter the number! ")
        continue
    if user_guess==random_number:
        print("Congrtulations: You guess the number!!")
        break
    elif user_guess>random_number:
            print("you are above the number ")
    else:
            print("you are below the number")
    
print("you guess number in",guesses,"times")
