import random
word_list = ["aardvark", "baboon", "camel"]

choosen_word = random.choice(word_list)
word_length = len(choosen_word)
display = []

for _ in range(word_length):
    display += "_"
print(display)



guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = choosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)

