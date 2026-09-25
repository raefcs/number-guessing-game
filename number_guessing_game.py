import random

computers_num = random.randint(0, 1000)


def check_guess(users_guess):
	while int(users_guess) != int(computers_num):
		if int(users_guess) > int(computers_num):
			print("Guess lower. ")
			users_guess = input("Next guess? ")
		elif int(users_guess) < int(computers_num):
			print("Guess higher. ")
			users_guess = input("Next guess? ")
	return print("Correct!, the number was " + str(computers_num) + ".")


users_guess = input(" Try and guess the computers number(1 - 1000): ")



print(check_guess(users_guess))
	
	