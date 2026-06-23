import random

class WordScrambleGame:
    def __init__(self):
        # A list of secret words to choose from
        self.words = ["python", "computer", "keyboard", "program", "science", "coffee", "nature","developer","office"]
        self.secret_word = ""
        self.scrambled_word = ""
        self.attempts = 0

    def scramble(self, word):
        # Turns the word into a list of letters, mixes them, and joins them back
        letter_list = list(word)
        random.shuffle(letter_list)
        return "".join(letter_list)

    def reset_game(self):
        # Resets the game state for a new round
        self.secret_word = random.choice(self.words)
        self.scrambled_word = self.scramble(self.secret_word)
        self.attempts = 3

    def play(self):
        print("Welcome to the Word Scramble Game!")
        
        play_on = True
        while play_on:
            # Set up a fresh round
            self.reset_game()
            
            print(f"\nUnscramble this word: {self.scrambled_word}")
            print(f"You have {self.attempts} attempts.\n")

            round_active = True
            while round_active and self.attempts > 0:
                # Take user input, strip spaces, and make it lowercase
                guess = input("Your guess: ").strip().lower()

                # Check if the guess is correct
                if guess == self.secret_word:
                    print(f"Correct! The word was indeed '{self.secret_word}'!")
                    round_active = False
                    continue

                # Handle incorrect guess
                self.attempts -= 1
                if self.attempts > 0:
                    print(f"Wrong! Try again. Attempts left: {self.attempts}\n")
                else:
                    print(f"Game Over! The correct word was '{self.secret_word}'.")

            # Ask the user if they want to play again
            choice = input("\nDo you want to play again? [Y for yes / any other key exit]: ").strip().upper()
            if choice != "Y":
                play_on = False

        print("\nThanks for playing! Goodbye.")

# Run the game
if __name__ == "__main__":
    game = WordScrambleGame()
    game.play()
