print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
import random
number=random.randint(1,100)
print(number)
game_not_over=True
level=input("Choose a difficulty.Type 'easy' or 'hard':")
if level=='easy':
   lives=10
elif level=='hard':
    lives=5
print(f"You have {lives} attempts remaining to guess the number ")    
def guess(user_guess):  
  if user_guess>number:
      print("Too high")
  elif user_guess<number:
      print("Too low")
  elif user_guess==number:
        print("You win")
        print("You choose the correct number")
while game_not_over:
     user_number=int(input("Choose a number:"))
     guess(user_number)
     lives-=1
     print(f"The remaining lives {lives}")
     if lives<=0 or user_number==number:
        game_not_over=False
        if lives<=0:
            print("You lose..")
       