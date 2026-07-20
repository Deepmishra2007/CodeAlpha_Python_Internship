# ------------------------------------
# Project: Hangman Game
# Internship: CodeAlpha Python Internship
# Developed by: Deep Mishra
# ------------------------------------
import random

# List of predefined words
words = ["python", "apple", "computer", "college", "program"]

while True:
    secret_word = random.choice(words)
    guessed_word = ["_"] * len(secret_word)
    attempts = 6
    guessed_letters = []

    print("\n🎉 Welcome to Hangman!")
    print("Guess the hidden word.")

    while attempts > 0 and "_" in guessed_word:

        print("\nWord:", " ".join(guessed_word))
        print("Attempts left:", attempts)
        print("Guessed letters:", " ".join(guessed_letters))

        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter only one alphabet.")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
            print("✅ Correct!")
        else:
            attempts -= 1
            print("❌ Wrong guess!")

    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
    else:
        print("\n💀 Game Over!")
        print("The word was:", secret_word)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("👋 Thanks for playing!")
        break