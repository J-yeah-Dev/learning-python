import random
names = {'r': 'Rock', 'p': 'Paper','s': 'Scissors' }
beats = {'r': 's', 'p': 'r','s': 'p' }
print("========== Play Rock, Paper, Scissors ==========")
while True:
    user_choice= input("What do yo choose: r for Rock, p for Paper, s for Scissors \n")
    while True:
        if user_choice in names:
            break;
        else:
            user_choice= input("Invlaid choice! Try Agian [Hint r : Rock, p : Paper, s : Scissors] \n")
          
    computer_choice = random.choice(['r', 'p', 's'])
    print(f"you chose: {names[user_choice]}")
    print(f"computer chose: {names[computer_choice]}")
    
    if user_choice ==  computer_choice :
        print("Its a Tie")
    elif beats[user_choice] == computer_choice:
        print("You win!")
    else:
        print("Computer win")
    
    print("-" * 20)
    again = input("Do you want to play again? (y/n): ").lower().strip()
    print("-" * 20)
    
    if again != 'y':
        print("Thanks for playing! Goodbye.")
        break
    
