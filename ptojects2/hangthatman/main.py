#hangman project
#my version
import random
import hangman
print(hangman.logo)
word_lst = hangman.word_lst
word = random.choice(word_lst).lower()
chosen_word = list(word)
num = len(word)
blanks = '-' * num
blanks_lst = list(blanks)
print(blanks)
lives = 6
user_gs_list = []


while lives > 0:
    user_gs = input("Guess a letter: ").lower()
    if user_gs in user_gs_list:
        print("You have already entered that letter before.")
    else:
        posn_lst = []
        count = 0
        user_gs_list.append(user_gs)

        for position in range(0,num):
            if chosen_word[position] == user_gs:
                posn_lst.append(position)

        if user_gs not in word:
            lives -= 1
            print(f"You guessed {user_gs}, that's not in the word. You lose a life.")

        for i in posn_lst:
            blanks_lst[i] = user_gs
        print(*blanks_lst,sep='')



        if lives == 6:
            print('''
      +---+
      |   |
          |
          |
          |
          |
    =========''')
        elif lives == 5:
            print('''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''')
        elif lives == 4:
            print('''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''')
        elif lives == 3:
            print('''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''')
        elif lives == 2:
            print('''
     +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''')
        elif lives == 1:
            print('''
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========''')
        else:
            print('''
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========''')

        print(f'you have {lives} lives left.')
        if '-' not in blanks_lst:
            break
        else:
            continue


if '-' in blanks_lst:
    print(f'you lose,the correct word was {word}.')
else:
    print('you win')