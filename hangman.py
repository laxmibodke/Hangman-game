#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen
import random
from hangman_words import word_list
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
end_of_game=False
lives=6

#TODO-2 - Replace the blanks in the display with the guessed letter.
display=[]
for _ in range(word_length):
    display+="_" 

#TODO-3 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
while not end_of_game:
    guess=input("Guess a letter:").lower()

    if guess in display:
        print(f"You've have already guessed {guess} ")
    #TODO-4 - Check if the letter the user guessed (guess) is one of the letters in
    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter 
    
    if guess not in chosen_word:
        print(f"You've have guessed {guess}, that's not in the word. You lose a life")
        lives-=1
        if lives==0:
            end_of_game=True
            print(f"You lose, The word is {chosen_word}")
    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("You win")
    print(stages[lives])
    

   