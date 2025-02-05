import random
from os import system, name

def clear_screen():
    # For Microsoft Windows
    if name == 'nt':
        _ = system('cls')
    
    # For Mac and Linux (here, os.name is 'posix')
    else:
        _ = system('clear')

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
         
def lettercount(text): # finds words in strings
    count = 0
    text = text.lower()
    for word in text.split():
        if "owl" in word: # put word to find in text in the quotes
            count += 1
    return count



game_over = False


word = random.choice(words)
prevgues = [ ]
hiddenword = "_" * len(word)
count = -1
tries = 0
hiddenword = list(hiddenword)

def previousgues():
    for i in range(len(prevgues)):
        pgues = prevgues[i] + " ,"
    return pgues 

while game_over == False:
    print(f"There are {len(word)} letters in the word. Guess a letter: ")
    print(HANGMANPICS[tries])
    print("Word:", hiddenword)
    prevgues.sort()
    print("Previous guesses:", prevgues)
    print(word)#fdgilukdfhgyidfsuhisdfhgoisdfgkjlsdfhiousdfigudfhoiudsfhgdfhiguhsdflighsdfoiguhldifuhgosidfhgoisdfuhgoisdfghio
    guess = input("Letter to guess?: ")
    prevgues.append(guess)

    if guess in word:
        for letter in word:
            
            print(count)
            #if count >= len(hiddenword):
                #count = -1
                #break
            if letter == guess:
                count += 1
                hiddenword[count] = guess


    elif guess not in word:
        tries += 1

    clear_screen()


    if tries == 6:
        print("GAME OVER, HANGMAN DIED.")
        playagain = input("Play again? (y/n): ")
        if playagain == "n":
            game_over = True
        elif playagain == "y":
            game_over = False
            tries = 0
            count = -1
            prevgues = []
            word = random.choice(words)
            prevgues = [ ]
            hiddenword = "_" * len(word)
            hiddenword = list(hiddenword)
        else:
            playagain = input("Play again? (y/n): ")
    