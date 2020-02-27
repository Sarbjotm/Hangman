
def guessing_letter():
	while True:
		global guess;
		guess = input("What letter do you guess: ");
		if not guess.isalpha():
			print("Try Again. \n");
			continue;

		else:
			if (len(guess) > 1):
				print("This is not a single letter, try again: ");
				continue
			else:
				guess = guess.lower();
				if (guess in letters_guessed):
					print("You have guessed that letter, try again: ");
					continue

				letters_guessed.append(guess);
				break;

def correct_letter():
	if guess not in word:
		global incorrect_guesses;
		incorrect_guesses = incorrect_guesses + 1;
		return;

	else:
		for i in range(0,len(word)):
			if word[i] == guess:
				word_guessed[i] = guess;
	return;
			

word = "banana";
word_guessed = [];
letters_guessed = [];
incorrect_guesses = 0;

for i in range(0,len(word)):
	word_guessed.append('_');
	print(word_guessed[i], end =" ");

print("\n");


while(incorrect_guesses < 5):
	guessing_letter();
	correct_letter();
	print(word_guessed);
	print(incorrect_guesses);

