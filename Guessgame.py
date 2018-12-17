import random
magic_word = ("flamingo")
guess_count = 0
guess_limit = 4
out_of_guesses = False
hints = ["They aren't tall but they can be up to 5ft wide.", "Think, red + white = what?", "When they eat, their head is positioned upside-down", "It isn't a dog", "You wont find them in the old world.", "Don't ask one to dance, it wants to stand on one leg."]
print("""Welcome to the guessing game. You will have five attempts to guess the magic word.""")
guess = input("What is your guess?:")
while guess != magic_word and not (out_of_guesses):
    if guess_count < guess_limit:
        hint = random.choice(hints) 
        print("Hint: "+ hint)
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lose!")
else:
    print("You win!")
