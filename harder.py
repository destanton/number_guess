import random


def number_game():
    print("Hello, I want you to pick a number, I'm going to try to guess it!")
    print("I only get a total of 5 guesses -- good luck!")
    random_number = int(input("Guess a number between 1 and 20: "))
    guesses = 0
    low = 1
    high = 20

    while guesses < 5:
        computer_guess = random.randint(low, high)
        input()
        guesses += 1
        print("I guessed: {} ".format(computer_guess))

        if computer_guess < random_number:
            low = computer_guess + 1
            print("Your guess is {} and my guess is {}".format(random_number, computer_guess))
        elif computer_guess > random_number:
            high = computer_guess - 1
            print("Your guess is {} and my guess is {}".format(random_number, computer_guess))
        elif computer_guess == random_number:
            print("Game over! I guessed {}, the same number as you! I WIN!".format(computer_guess))
            print("I took a total of {} guesses".format(guesses))
            break
    else:
        print("I guessed wrong {} times. Game Over".format(guesses))
number_game()
