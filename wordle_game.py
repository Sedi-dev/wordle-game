#simple wordle clone 
#Lesedi Mohale
#07 April 2026 

import random
with open("words.txt") as f:
   words = [word.strip() for word in f if len(word.strip()) == 5]

def wordle(user_guess, target):
   
   results_list = ['-','-','-','-','-']
   remaining_letters = list(target)
   
   for i in range(len(user_guess)):
      
      if user_guess[i] == target[i]:
         results_list[i] = '*'
         remaining_letters[i] = None
   
   for k in range(len(user_guess)):
         if results_list[k] == '-':
            if user_guess[k] in remaining_letters: 
               results_list[k] = '+' 
               remaining_letters.remove(user_guess[k])
               
   return ''.join(results_list)

def main():
   
   target = random.choice(words).lower()
   user_guess = ''
   won = False
   
   for _ in range(6):
      user_guess = input('Please enter your word:\n').lower()
      
      if len(user_guess) != 5:
         print("Only 5 letter guesses are allowed!")
         continue
      
      if user_guess not in words:
         print("Not a valid word ❌")
         continue      
            
      result = wordle(user_guess, target)
         
      
      print(result)
      
      if user_guess == target:
         print("You got it!!🥳")
         won = True
         break
         
   if not won:
      print("You'll get it next time :-)")
   
   print("Words was:", target)
    
if __name__ == '__main__':
      main()

    