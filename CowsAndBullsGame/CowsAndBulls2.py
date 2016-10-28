# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place, they have a cow. 
# For every digit the user guessed correctly in the wrong place is a bull. 
# Every time the user makes a guess, tell them how many cows and bulls they have. 
# Once the user guesses the correct number, the game is over. 
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end

import time
import sys

from random import randint

def main():
	
	cow = 0
	bull = 0
	round = 0
	cow_position = [0,0,0,0]
	bull_position = [0,0,0,0]
	num = str(randint(1000,9999))

	print("Let's play a game of Cowbull!\n") #explanation
	time.sleep(2)
	print("I will generate a number, and you have to guess the numbers one digit at a time.\n")
	time.sleep(2)
	print("For every number in the wrong place, you get a bull. For every one in the right place, you get a cow.\n")
	time.sleep(2)
	print("The game ends when you get 4 cows!\n")
	time.sleep(2)
	print("Type q at any prompt to exit.\n")
	time.sleep(2)

	while True:
		n = raw_input("please guess a 4-digit number: ")
		if n=='q':
			break
		if n=="show":
			print("HAHA! ARE YOU GIVING UP?")
			print "The Result is: "+num
			break
		if(len(n)!=4):
			continue

		else:
			round = round +1
			print ("Round %d result \n" %round)

			for i in range(len(num)):
				if num[i] in n:
					if(n[i]==num[i]):
						cow_position[i] = 1
						bull_position[i] = 0
					else:
						cow_position[i] = 0
						bull_position[i] = n.count(num[i])-cow_position[i]
				else:
					cow_position[i] = 0
					bull_position[i] = 0

			cow = cow_position.count(1)
			bull = sum(bull_position)
			if cow == 4:
				print ("YOU GET IT!!!")
				break
			print "you have %d cow" %cow
			print "you have %d bull" %bull


if __name__ == '__main__':
	main()
	raw_input("Press ENTER to exit ...")
	
