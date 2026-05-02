#simple wordle clone 
#Lesedi Mohale
#07 April 2026 

import random

#Load all valid 5-letter words from the file
with open("words.txt") as f:
   words = [word.strip() for word in f if len(word.strip()) == 5]

def evaluate_guess(user_guess, target):
   """
   Compare the user's guess to the target word and return feedback.
   
   '*' = correct letter in the correct position
   '+' = correct letter in the wrong position
   '-' = letter not in word
   
   This function also handles duplicate letters correctly.
   """
   
   # Start with all positions marked as incorrect
   results_list = ['-','-','-','-','-']
   
   # Convert target to a list so we can "use up" letters as they are matchec
   remaining_letters = list(target)
   
   # First pass: check for correct letters in correct positions
   for i in range(len(user_guess)):
      
      if user_guess[i] == target[i]:
         results_list[i] = '*'
         remaining_letters[i] = None
   
   # Second pass: check for correct letters in wrong positions 
   for k in range(len(user_guess)):
         if results_list[k] == '-':    # Only check letters not already matched
            if user_guess[k] in remaining_letters: 
               results_list[k] = '+' 
               remaining_letters.remove(user_guess[k])  # Prevent reuse
               
   return ''.join(results_list)

def main():
   """
   
   Main game loop:
   - Selects a random word
   - Allows up to 6 guesses
   - Validates input
   - Displays feedback after each guess
   """
   
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
            
      result = evaluate_guess(user_guess, target)
         
      
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

    