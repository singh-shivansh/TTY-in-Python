def guess_game():
    from random import randint

    random_number = randint(1, 10)

    guesses_left = 3
    while guesses_left > 0:
        guess=int(input("Enter your guess:"))
        if guess==random_number:
            print("You win")
            break
        guesses_left-=1
    else:
        print("You lose")
        print("The number was",random_number)

guess_game()