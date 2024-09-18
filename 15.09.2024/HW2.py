# START
import random

number = random.randint(1, 100)
counter = 0
while True:
    num_guess: int = int(input("Guess the correct number: "))
    counter += 1
    if number > num_guess:
        print("your number is too small.")
    elif number < num_guess:
        print("your number is too big.")
    else:
        print(f"BINGO, you guessed {counter} times. ")
        break

        # STOP
