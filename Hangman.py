import random
import hangman_words
import art

word = random.choice(hangman_words.wordlist)
word_length = len(word)

display = ["_"] * word_length
lives = 6
end_of_game = False

print("Welcome to The Game of Hangman!")
print(art.logo)
print(art.stages[lives])
print(" ".join(display))

while not end_of_game:
    user_guess = input("Guess a letter: ").lower()

    if user_guess in display:
        print(f"You've already guessed {user_guess}")

    for position in range(word_length):
        letter = word[position]
        if letter == user_guess:
            display[position] = letter

    if user_guess not in word:
        lives -= 1
        print(f"Letter {user_guess} is not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The word was: {word}")

    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("You win!")
        print(f"The word was: {word}")

    print(art.stages[lives])
