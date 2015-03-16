# Variables are initialised before called in the program
guess = 50
answer = 0
top = 100
base = 0

# User is informed of the concept
print("Please think of a number between 0 and 100!")

# While loop is created to repeat steps of guessing the number
while answer != 'c':
    answer = raw_input("Is your secret number %s? \n",
    "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " % (guess))
 
    if answer == "h":
        top = guess
        guess = (base + ((top - base)/2))

    elif answer == "l":
        base = guess
        guess = (base + ((top - base)/2))

    elif answer == "c":
        break
            
    else:
        print("\n Sorry, I did not understand your input.")

print("Game over. Your secret number was: " + str(guess))