#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from replit import clear
from art import logo
EASY=10
HARD=5
def  check_number(guess,answer,turns):
  if guess>answer:
    print("too high")
    return turns-1
  elif guess<answer:
    print("too low")
    return turns-1
  else:
    print(f"you win,your answer is{answer}")

  


def set_attempts():
  choose=input("type'easy; or'hard' : ")
  if choose=="easy":
    return EASY
  else:
    return HARD

 
def play_game():
  print("welcome to the number of games")
  print("i am, thinking opf a number between 1 and 100")
  answer=random.randint(0,100)
  print(f"psssst ,the correct answer is{answer}")
  turns=set_attempts()
   
  guess=0
  while guess!=answer:
    print(f"you have {turns} attempts remaining to guess the number" )
    guess=int(input("make a guess: "))
    
    turns=check_number(guess,answer,turns)
  
    if turns==0:
      print("you run out of a game,you lose")
      return
      
     
     
play_game()  