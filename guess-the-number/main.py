import random
number = random.randint(1,100)
print("***** Welcome to Guess the Number Game *****")
print("The number is ready. Are you ready to guess?")
guess = int(input("Guess the number:"))
count=0
while guess != number:
    if guess > number:
        print("Too high! Try again")
    elif guess < number:
        print("Too low! Try again")
    count+=1
    guess = int(input("Guess the number:"))
print(f"Yay! You guessed the correct number in {count} guesses")
