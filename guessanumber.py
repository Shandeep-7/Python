#Game : Guess the number
import random

easy_attempts = 10
hard_attempts = 5

def difficulty(level_ch):
    if level_ch == 'easy':
        return easy_attempts
    else:
        return hard_attempts
    
def check_ans(guess,ans,attempts):
    if guess < ans:
        print("Your guess is too low")
        return attempts-1
    elif guess > ans:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"Your answer is right and answer was {ans}.")

def game():
    print("Let me think of a number between 1 -> 50")
    ans = random.randint(1,50)
    level = input("Choose difficulty easy or hard : ")
    attempts=difficulty(level)
    guess=0
    while guess != ans:
        print(f"you have {attempts} attempts remaining")
        guess = int(input("Guess an number : "))
        attempts = check_ans(guess,ans,attempts)
        if attempts == 0:
            print("Your have lost your attempts... You lose!")
            return
        elif guess!=ans:
            print("Try again")
            
game()