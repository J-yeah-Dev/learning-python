import random

class WordGuessGame:
    def __init__(self):
        self.word_pool = ["python", "variable", "function", "compiler", "algorithm", "developer", "sequence", "computer", "program"]
        self.secret_word = random.choice(self.word_pool).lower()
        self.guessed_letters = set()
        self.max_attempts = 6
        self.wrong_attempts = 0

    def get_display_word(self):
        """Returns the word with underscores for unguessed letters."""
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.secret_word])

    def process_guess(self, letter):
        """Processes the user's input and updates game state."""
        letter = letter.lower().strip()

        # Input validation
        if not letter.isalpha() or len(letter) != 1:
            return "Invalid input. Please enter exactly one alphabetical letter."
        
        if letter in self.guessed_letters:
            return f"You already guessed '{letter}'. Try a different one!"

        # Add to guessed list
        self.guessed_letters.add(letter)

        # Check if letter is in the secret word
        if letter in self.secret_word:
            return f"Good job! '{letter}' is in the word."
        else:
            self.wrong_attempts += 1
            return f"Incorrect! '{letter}' is not in the word."

    def is_won(self):
        """Checks if all letters have been guessed."""
        return all(letter in self.guessed_letters for letter in self.secret_word)

    def is_game_over(self):
        """Checks if the game has ended (win or loss)."""
        return self.is_won() or (self.wrong_attempts >= self.max_attempts)


# --- Game Loop Execution ---
print("=== WELCOME TO THE WORD GUESSER ===")
game = WordGuessGame()

print("Can you guess the secret programming-related word?")

# Keep playing until won or out of attempts
while not game.is_game_over():
    print(f"\nWord to guess: {game.get_display_word()}")
    print(f"Attempts remaining: {game.max_attempts - game.wrong_attempts}")
    print(f"Guessed letters: {', '.join(sorted(game.guessed_letters)) if game.guessed_letters else 'None'}")
    
    user_input = input("Guess a letter: ")
    feedback = game.process_guess(user_input)
    print(feedback)

# Final game over check
print("\n=== GAME OVER ===")
if game.is_won():
    print(f"Congratulations! You guessed the word: '{game.secret_word}'!")
else:
    print(f"Out of attempts! The correct word was: '{game.secret_word}'.")
