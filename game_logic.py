import random

from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])

    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)
    print("Word:", display_word)
    print()


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print("You saved the snowman!")
            break

        if mistakes >= max_mistakes:
            print("Game Over! The word was:", secret_word)
            break

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1


def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower().strip()
        if again != "y":
            break


if __name__ == "__main__":
    main()