import random
magic_word = ("cat")
guess_count = 0
guess_limit = 3
out_of_guesses = False
def hint_help():
  hints = ["It has four legs", "It says 'meow'", "It's likes milk"]
  random.shuffle(hints)
  for hint_function in hints:
    hint_function()
print("""Welcome to the guessing game. 
You will have three attempts to guess the magic word.""")
guess = input("What is your guess?:")
while guess != magic_word and not (out_of_guesses):
    if guess_count < guess_limit:
        hint_help()
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lose!")
else:
    print("You win!")
