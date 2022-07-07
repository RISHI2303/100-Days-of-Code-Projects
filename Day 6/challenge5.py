import random
from hangman_art import stages
from hangman_words import word_list

from hangman_art import logo
print(logo)

chosen_word = random.choice(word_list)
display = []
lives = 6
end_of_game = False

for i in range(len(chosen_word)):
    display += '_'

count = len(chosen_word)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    flag = 0

    # Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == display[position]:
            print(f"You have already guessed {guess}")
        if letter == guess:
            display[position] = letter
            flag = 1

    if flag == 0:
        print(f"You guessed {guess}, that's not in the word. You loose a life.")
        lives -= 1

    if lives == 0:
        print("You lose")
        print(f"The word was: {chosen_word}")
        end_of_game = True

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(f"{stages[lives]}")
