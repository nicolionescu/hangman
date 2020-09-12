import random

print('H A N G M A N')

lives = 8
words = ['python', 'java', 'kotlin', 'javascript']
r_word = random.choice(words)
hidden_letters = ['-'] * len(r_word)
used_letters = []

while lives > 0:
  print()
  print (str.join('', hidden_letters))
  guess = input('Input a letter: ')

  if len(guess) != 1:
    print("You should input a single letter")
    continue

  if guess.isalpha() == False or guess.isupper():
      print("It is not an ASCII lowercase letter")
      continue
  
  if guess in used_letters:
    print('You already typed this letter')
    continue
  
  used_letters.append(guess)
  
  if guess in r_word:
    for i in range(len(r_word)):
      if r_word[i] == guess:
        hidden_letters[i] = guess
  else:
    print('No such letter in the word')
    lives -= 1

  if str.join('', hidden_letters) == r_word:
      print()
      print(str.join('', hidden_letters))
      print('You guessed the word!\nYou survived!')
      break
  elif str.join('', hidden_letters) != r_word and lives == 0:
      print('You are hanged!')
      break