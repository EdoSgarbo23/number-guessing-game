import random

print("Hi, welcome to number guessing game. You've got 7 chances to guess the number between 0 and 100. Good luck :) ")

number_to_guess = random.randrange(100)


chances = 7

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input("Please enter your guess: "))

    if my_guess == number_to_guess: 
        print("The number is", number_to_guess, "and you got it right! You did it in", guess_counter, "attempts")
        break
    elif guess_counter >= chances and my_guess != number_to_guess :
        print("Sorry, the number was:"), print(number_to_guess), print("Better luck next time!")

    elif my_guess > number_to_guess : 
        print("Your guess is higher. Try again ")

    elif my_guess < number_to_guess :
        print("Your guess is lower. Try again ")