import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        # Ask the user for their guess
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Compare the guess to the generated number
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts!")
            break

# Run the game
number_guessing_game()
