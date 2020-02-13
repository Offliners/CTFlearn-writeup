# I DID NOT CREATE THE ORIGINAL GAME, BUT John_123 created it.
# Link: https://repl.it/@John_123/Lazy-Game

# Modified by theKidOfArcrania
# Changelog from John_123's version:
# - I decreased sleep times (they were a little bit of a 
#   nuisance to wait).
# - Made the input be case insensitive (if you type in 'y'
#   it will not register this as yes response).
# - Fix OBOE error when user gets 11th guess (but it doesn't 
#   count).
# - Added a millionare challenge!


import random
import replit
from termcolor import cprint
import time 

replit.clear()

cprint('Welcome to the Game of Luck !. ','cyan',attrs=['blink'])

cprint('\nRules of the Game :','red')

print("""(1) You will be Given 500$
(2) Place a Bet
(3) Guess the number what computer thinks of !
(4) computer's number changes every new time !.
(5) You have to guess a number between 1-10
(6) You have only 10 tries !.
(7) If you guess a number > 10, it still counts as a Try !
(8) Put your mind, Win the game !..
(9) If you guess within the number of tries, you win money !
(10) Good Luck !..

theKidOfArcrania:
  I bet you cannot get past $1000000!""")

opinion2 = 'Y'
wallet = 500

opinion = input(('\n\nAre you ready? Y/N : ' )).upper()

while opinion2 == 'Y' :
  if opinion == 'Y':
    replit.clear()
    dup = wallet
    cprint('Money you have','red' ,end='')
    cprint(' : ',end='')
    cprint(str(dup)+'$','green')
    spent = int(input('Place a Bet : '))
    while spent > dup:
      cprint('Money you have','red' ,end='')
      cprint(' : ',end='')
      cprint(str(dup),'green')
      print('\n\nYou don\'t have that much')
      print('Enter only from what you have !.')
      replit.clear()
      spent = int(input('Place a Bet : '))
  
  
    replit.clear()  
    cprint('Loading .. ')
    time.sleep(.5) # decrease delays
  
    replit.clear()
    square = '⬛'
    for i in range(1,21):
      print('Loading : '+square*i , 5*i,'%')
      time.sleep(.2)
      if i == 20:
        time.sleep(1)
      replit.clear()
    
    # Switched the ordering of statements so that user only
    # gets 10 guesses
    #######   *     #          #######     ##    #
   #      #    #    #####     #       #__#  #   
   #      #     #             #      #   #   #

    for a in range(10):
      guess = int(input('\n\nMake a Guess : '))
      x = random.randint(1,10)
      print('\n\nComputer\'s number : ',x)
      print('Your Guess : ',guess)
      print('Sorry Wrong Guess, Try Again !. -_- ')
      time.sleep(.5)
      replit.clear()
      
      if x == guess:
        break
    if x == guess :
      wallet += 2*spent
      print('\n\nYou made it !.')
      print('You won JACKPOT !..')
      print('You thought of what computer thought !.')
      print('Your balance has been updated !')
      if wallet >= 1000000:
        wallet = 999999 # You don't get more than $999,999
      
      cprint('\n\nCurrent balance','red',end='')
      cprint(' : ',end='')
      cprint(str(wallet)+'$','green',attrs=['blink'])
    else:
      wallet -= spent
      print('Sorry you didn\'t made it !')
      print('Play Again !...')
      print('Better Luck next Time !.')
      time.sleep(1)
      print('Sorry you lost some money !..')
      print('Your balance has been updated !.')
      cprint('Current balance : ','red',end='')
      cprint(' : ')
      cprint(str(wallet)+'$','green',attrs=['blink'])
    time.sleep(2)
    
  if wallet > 1000000:
    cprint('What the... how did you get that money (even ' +
    'when I tried to stop you)!? I guess you beat me!\n', 'cyan')
    break
  opinion2 = input('Want to play again? Y/N : ').upper()
  
cprint('Thank you for playing ! ','cyan')
cprint('Made by John_123','yellow',attrs=['blink'])
cprint('Small mods by theKidOfArcrania','red',attrs=['blink'])
cprint('Give it a (+1) if you like !..','cyan',attrs=['bold'])
    
