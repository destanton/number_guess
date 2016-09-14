import random


def number_game():
    computer_guess = random.randint(1, 20)
    guesses = 0
    print("Can you guess my number?")
    print("You get a total of 5 guesses")
    while guesses < 5:
        try:
            your_guess = int(input("Give me a number between 1 and 20: "))
            guesses += 1
        except ValueError:
            print("{} isn't a number".format(your_guess))
            continue
        else:
            if your_guess < computer_guess:
                print("My number is higher than {}, guess higher!".format(your_guess))
            elif your_guess > computer_guess:
                print("My number is lower than {}, guess lower!".format(your_guess))
            elif your_guess == computer_guess:
                print("GAME OVER! We tied, we both guessed {}!".format(your_guess))
                print("You took a total of {} guesses".format(guesses))
                break
    else:
        print("You guessed wrong {} times. Game Over".format(guesses))

number_game()
