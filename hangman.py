import random
from words import words

x=int()
word=(str)
display = list()
wordguess = 0

def startgame():
    global x
    global word
    global display
    x = random.randint(0, len(words))
    word = words[x]
    for letter in word:
        display.append("_")
    print("Welcome to hangman!\n"
          "Type 'quit' at any time to quit the game\n\n"
          "Your random word has been chosen.\n"
          "You can see how many letters are in it below.\n")
    print(display, "\n")

def replayfunc():
    global display
    global wordguess
    replay = input("Would you like to play again? y/n")
    replay = replay.casefold().strip()
    if replay == "y":
        display = []
        wordguess = 0
        startgame()
        playgame()
    elif replay == "n":
        print("K bye then <3")
        exit()
    else:
        print("Oops, you didn't type y or n.\n Blowing up now.\n...bye")
        exit()

def guesstheword():
    global wordguess
    global display
    if wordguess < 3:
        wordguess += 1
        answer = input("What do you think the word is?")
        if answer == word:
            print("*******************************\n"
                  "You did it! You win! Woohoo!\n"
                  "*******************************")
            replayfunc()
        elif answer != word and wordguess >= 3:
            print("Oh no! Wrong again... and you're out of guesses.\n"
                  f"The correct answer was '{word}'.\n"
                  "Better luck next time!")
            replayfunc()
        else:
            print("Oooh, not quite! Keep playing before you guess again!\n"
                  f"You have {3 - wordguess} turn(s) left to guess the full word!\n")
            print(display)

def playgame():
    if len(word) > 6:
        count = 9
    elif len(word) > 8:
        count = 10
    else:
        count = 8
    entries = list()
    while count > 0:
        guess = input("Take a guess! Type a single letter to see if it's there.\n"
                      "Or enter 'guess' to take a guess at the full word.")
        guess = guess.casefold().strip()
        if guess == "guess":
            guesstheword()
        elif guess == "quit":
            print("K bye then <3")
            exit()
        elif guess in entries:
            print("You've already guessed that letter! Here's the letters you've guessed so far:\n",entries,"\n")
        elif len(guess) > 1:
            print("***************************\n"
                  "Please enter a single character, or type 'guess' to guess the whole word.\n")
        elif not guess.isalpha():
            print("***************************\n"
                  "Please enter a single alphabet letter, or type 'guess' to guess the whole word.\n")
        else:
            entries.append(guess)
            count -= 1
            if count > 0:
                print(f"\nYou've got {count} letter guesses left and {3 - wordguess} chances to guess the word.\n")
            playguess(guess)
            if "_" not in display:
                print(display)
                print(f"That's right! The word was {guess}!")
                print("*******************************\n"
                      "You did it! You win! Woohoo!\n"
                      "*******************************")
                replayfunc()
            else:
                print(display)
                if count == 0:
                    print("\n\nYou're out of letter guesses!\n"
                          "This is your last chance...try to guess the word!\n")
                    guesstheword()
    print("\nOh no! ...you're out of guesses.\n"
          f"The correct answer was '{word}'.\n"
          "Better luck next time!")
    replayfunc()

def playguess(guess):
    global x
    global word
    global display
    for letter in range(len(word)):
        if guess in word[letter]:
            display[letter] = word[letter]
            print("You guessed a letter!")


startgame()
playgame()
