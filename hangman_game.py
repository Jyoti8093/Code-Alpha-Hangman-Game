import random

def hangman():
    # List of predefined words
    words = ["apple", "tiger", "house", "green", "light"]
    
    # Randomly select a word from the list
    word = random.choice(words)
    guessed = ["_"] * len(word)
    guessed_letters = []
    attempts = 6

    print("🎮 Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.")
    print("You have 6 incorrect attempts.\n")

    # Game loop
    while attempts > 0 and "_" in guessed:
        print("Word:", " ".join(guessed))
        print("Guessed letters:", " ".join(guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabetic character.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!\n")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}\n")

    # Game result
    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game over! The correct word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
