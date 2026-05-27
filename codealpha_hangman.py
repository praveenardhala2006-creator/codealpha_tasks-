import random

words = ["apple", "tiger", "chair", "robot", "house"]

word = random.choice(words)

 #Store guessed letters
guessed_letters = []

attempts = 6

display = ["_"] * len(word)

print("=== HANGMAN GAME ===")

while attempts > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")

        # Reveal correct positions
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        print("Wrong!")
        attempts -= 1

if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)