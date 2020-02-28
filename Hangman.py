
def guessing_letter():
	print("\n")
	while True:
		global guess
		guess = input("What letter do you want to guess: ")
		if not guess.isalpha():
			print("Try Again. \n")
			continue

		else:
			if (len(guess) > 1):
				print("This is not a single letter, try again: ")
				continue
			else:
				guess = guess.lower()
				if (guess in letters_guessed):
					print("You have guessed that letter, try again: ")
					continue

				letters_guessed.append(guess)
				break

def correct_letter():
	if guess not in word:
		global incorrect_guesses
		incorrect_guesses = incorrect_guesses + 1
		return

	else:
		for i in range(0,len(word)):
			if word[i] == guess:
				word_guessed[i] = guess
	return


def drawing_man():
	if (incorrect_guesses == 0):
				print("____________")
				print("|	 |")
				print( "|")
				print( "|")
				print( "|")
				print ("|")
				print ("|________", end = " ")
	if (incorrect_guesses == 1):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|")
				print ("|")
				print ("|")
				print ("|________", end = " ")
	elif (incorrect_guesses == 2):
			print ("_________")
			print ("|	 |")
			print ("|	 O")
			print ("|	 |")
			print ("|	 |")
			print ("|")
			print ("|________", end = " ")
	elif (incorrect_guesses == 3):
			print ("_________")
			print ("|	 |")
			print ("|	 O")
			print ("|	\\|")
			print ("|	 |")
			print ("|")
			print ("|________")
	elif (incorrect_guesses == 4):
			print ("_________")
			print ("|	 |")
			print ("|	 O")
			print ("|	\\|/")
			print ("|	 |")
			print ("|")
			print ("|________", end = " ")
	elif (incorrect_guesses == 5):
			print ("_________")
			print ("|	 |")
			print ("|	 O")
			print ("|	\\|/")
			print ("|	 |")
			print ("|	/ ")
			print ("|________", end = " ")
	elif (incorrect_guesses == 6):
			print ("_________")
			print ("|	 |")
			print ("|	 O")
			print ("|	\\|/")
			print ("|	 |")
			print ("|	/ \\")
			print ("|________", end = " ")



def printing_guessed_letters():
	print("\n")
	print("You have guessed: the letters: ", end = " ")
	for i in range(0,len(letters_guessed)):
		print(letters_guessed[i], end = " ")


def display_word():
	if len(word_guessed) == 0:
		for i in range(0,len(word)):
			word_guessed.append("_")

	print("\t", end = " ")
	for i in range(0,len(word)):
		print(word_guessed[i], end = " ")


def main():
	global word
	word = "banana"
	global word_guessed
	word_guessed = []
	global letters_guessed
	letters_guessed = []
	global incorrect_guesses
	incorrect_guesses = 0


	while(incorrect_guesses < 6):
		drawing_man()
		display_word()
		printing_guessed_letters()	
		guessing_letter()
		correct_letter()

	if(incorrect_guesses == 6):
		while True: 
			again = input("You have lost. Play Again?" )
			if not again.isalpha():
				print("Not valid answer, try again: ")
				continue
			elif(again.lower() == "yes" or again.lower() == "y"):
				main()
			elif (again.lower() == "no" or again.lower() == "n"):
				exit()
			else:
				print("Not a valid answer, try... again: ")
				continue
				

main()


	
