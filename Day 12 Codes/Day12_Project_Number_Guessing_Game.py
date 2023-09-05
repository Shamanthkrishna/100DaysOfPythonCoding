from random import randint

easy_level = 10
hard_level = 5

def check(guess, ans, turns):
    if guess > ans:
        print("Too High")
        return turns - 1
    elif guess < ans:
        print("Too Low")
        return turns - 1
    else:
        print(f"Yess you guessed it right. The number was {ans}")

def difficulty():
    level = input("Choose a Difficulty: Type easy or hard: ") 
    if level == "easy":
        return easy_level
    else:
        return hard_level

def game():
    print("Welcome to Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")

    ans = randint(1,100)

    turns = difficulty()
    
    guess = 0
    while guess != ans:
        print(f"You have {turns} attempts left")
        guess = int(input("Make a Guess: "))
        turns = check(guess,ans,turns)

        if turns == 0:
            print("You have run out of guesses, you lose")
            return
        elif guess!= ans:
            print("Guess again")

game()