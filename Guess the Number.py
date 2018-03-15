import random

tries = 3
numgen = random.randint(1,10)

print("")
name = input("Hello, what is your name?: ")
print("")
print("Nice to meet you " + str(name) + ", I'm thinking of a number between 1 and 10")

while tries != 0:
	print("")
	guess = int(input("Guess the number: "))
	tries = tries - 1

	if guess != numgen:
		print("")
		print("Incorrect!")
		print("You have this many tries left: " + str(tries))
	else:
		break

if guess != numgen:
	print("")
	print("You SUCK " + str(name) + "..")
	print("")
	print("Better luck next time! The number was: " + str(numgen))
if guess == numgen:
	print("")
	print("Correct! You guessed right!")
