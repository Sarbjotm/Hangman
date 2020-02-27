word = "banana";
word_guessed = [];
letters_guessed = [];

for i in range(0,len(word)):
	word_guessed.append('_');


for i in range(0,len(word)):
	print(word_guessed[i], end =" ");

print("\n");
s = 1;
while(s < 5):
	guess = input();
	letters_guessed.append(guess);
	if (guess in word):
		for i in range(0,len(word)):
			if guess == word[i]:
				word_guessed[i] = guess;
				
	for i in range(0,len(word)):
		print(word_guessed[i], end =" ");
s = s+1;


