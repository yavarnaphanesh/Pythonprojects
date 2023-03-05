# HangMan Code
import random
words = ['phani', 'king', 'lucky', 'bujji']
hangman = ['''  _______
     |/      |
     |       o
     |      \|/
     |       |
     |      / \
     |
 ____|___''', '''  _______
     |/      |
     |       o
     |      \|/
     |       |
     |      / \
     |
 ____|___''']
Word_to_be_guessed = random.choice(words)
print(Word_to_be_guessed)
display = []

for _ in Word_to_be_guessed:
    display.append("_")


l = len(Word_to_be_guessed)
g = 0
while g<l:
    user_input = input("Guess a letter: ").lower()
    for position in range(l):
        letter = Word_to_be_guessed[position]
        if letter == user_input:
            display[position] = letter
    print(display)
    g += 1
list_word = [str(x) for x in Word_to_be_guessed]
if "_" not in display:
    print("You won")
else:
    print("You loose")















































































