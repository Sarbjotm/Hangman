
def guessing_letter():
	print("\n")
	while True:
		global guess
		guess = input("What letter do you want to guess: ")
		if not guess.isalpha():
			print("That is not a character, try again \n")
			time.sleep(0.5)
			clear()
			drawing_man()
			display_word()
			printing_guessed_letters()
			print("\nReminder your category is: ", category)
			print("\n")
			continue

		else:
			if (len(guess) > 1):
				print("This is not a single letter, try again: ")
				time.sleep(0.5)
				clear()
				drawing_man()
				display_word()
				printing_guessed_letters()
				continue
			else:
				guess = guess.lower()
				if (guess in letters_guessed):
					print("You have guessed that letter")
					time.sleep(2)
					clear()
					drawing_man()
					display_word()
					printing_guessed_letters()
					print("\nReminder your category is: ", category)
					print("\n")
					continue

				letters_guessed.append(guess)		
				for i in range(0, len(letters_guessed)):
					for j in range(i+1,len(letters_guessed)):
						if letters_guessed[i] > letters_guessed[j]:
							tmp = letters_guessed[i]
							letters_guessed[i] = letters_guessed[j]
							letters_guessed[j] = tmp
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
				print("____________")
				print ("|	 |")
				print ("|	 O")
				print ("|")
				print ("|")
				print ("|")
				print ("|________", end = " ")
	elif (incorrect_guesses == 2):
			print("____________")
			print ("|	 |")
			print ("|	 O")
			print ("|	 |")
			print ("|	 |")
			print ("|")
			print ("|________", end = " ")
	elif (incorrect_guesses == 3):
			print("____________")
			print ("|	 |")
			print ("|	 O")
			print ("|	\\|")
			print ("|	 |")
			print ("|")
			print ("|________", end = " ")
	elif (incorrect_guesses == 4):
			print("____________")
			print ("|	 |")
			print ("|	 O")
			print ("|	\\|/")
			print ("|	 |")
			print ("|")
			print ("|________", end = " ")
	elif (incorrect_guesses == 5):
			print("____________")
			print ("|	 |")
			print ("|	 O")
			print ("|	\\|/")
			print ("|	 |")
			print ("|	/ ")
			print ("|________", end = " ")
	elif (incorrect_guesses == 6):
			print("____________")
			print ("|	 |")
			print ("|	 O")
			print ("|	\\|/")
			print ("|	 |")
			print ("|	/ \\")
			print ("|________", end = " ")



def printing_guessed_letters():
	print("\n")
	print("You have guessed the letters: ", end = " ")
	for i in range(0,len(letters_guessed)):
		print(letters_guessed[i], end = " ")


def display_word():
	if len(word_guessed) == 0:
		for i in range(0,len(word)):
			word_guessed.append("_")

	print("\t", end = " ")
	for i in range(0,len(word)):
		print(word_guessed[i], end = " ")

def clear():
	os.system("clear")

def check_if_win():
	for i in range(0,len(word)):
		if(word_guessed[i] != word[i]):
			return 0
	return 1

def main():
	global category
	global word
	while True:
		category = input("What word category would you like to use, Nouns, Verbs or Adjectives: ")
		if not category.isalpha():
			print("Not a Valid Answer, try again: ")
			continue
		elif (category.lower() == "nouns" or category.lower() == "verbs" or category.lower() == "adjectives"):
			break
		else:
			print("Enter nouns, verbs or adjectives, try again: ")
			continue

	

	global word_guessed
	word_guessed = []
	global letters_guessed
	letters_guessed = []
	global incorrect_guesses
	incorrect_guesses = 0
	line_number = random.randint(1,50)
	word = linecache.getline(category+".txt", line_number)
	word = word.strip("\n")
	#print("The word is: ", word) #Used for Testing

	while(incorrect_guesses < 6):
		drawing_man()
		display_word()
		printing_guessed_letters()
		print("\nReminder your category is: ", category)	
		guessing_letter()
		correct_letter()
		if (check_if_win()):
			break
		clear()	

	if(incorrect_guesses == 6):
		drawing_man()
		display_word()
		printing_guessed_letters()	
		while True: 
			again = input("\nYou have lost. The word was " + '\033[1m' + word + '\033[0m' + ". Play Again? Answer Yes(y) or No(n): " )
			if not again.isalpha():
				print("Not valid answer, try again: ")
				continue
			elif(again.lower() == "yes" or again.lower() == "y"):
				clear()
				main()
			elif (again.lower() == "no" or again.lower() == "n"):
				exit()
			else:
				print("Not a valid answer, try again: ")
				continue
	else:
		clear()
		drawing_man()
		display_word()
		printing_guessed_letters()	
		while True: 
			again = input("\nYou have won! Play Again? Answer Yes(y) or No(n): " )
			if not again.isalpha():
				print("Not valid answer, try again: ")
				continue
			elif(again.lower() == "yes" or again.lower() == "y"):
				clear()
				linecache.clearcache()
				main()
			elif (again.lower() == "no" or again.lower() == "n"):
				linecache.clearcache()
				exit()
			else:
				print("Not a valid answer, try again: ")
				continue

				
import os
import random
import linecache
import time
clear()
main()


	
