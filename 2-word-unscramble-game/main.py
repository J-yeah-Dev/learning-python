import random
word_list = ["climb", "civic", "fuzzy", "juicy", "jumbo","lymph","pixel" "waltz"]
word = random.choice(word_list)
scrambled = "".join(random.sample(word, len(word)))
print(f"Unscramble this word: {scrambled}")
guess = input("Your guess: ").lower()
if guess== word:
    print("Correct! You got it.")
else:
    print(f"Wrong! The correct word was: {word}")
