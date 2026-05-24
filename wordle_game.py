#simple wordle clone 
#Lesedi Mohale
#07 April 2026 

import random


max_attempts = 6
word_length = 5

#Load all valid 5-letter words from the file
with open("words.txt") as f:
   WORDS = [word.strip().lower() for word in f if len(word.strip()) == word_length]

def evaluate_guess(user_guess, target):
   """
   Compare the user's guess to the target word and return feedback.
   
   '*' = correct letter in the correct position
   '+' = correct letter in the wrong position
   '-' = letter not in word
   
   This function also handles duplicate letters correctly.
   """
   
   # Start with all positions marked as incorrect
   feedback = ['-'] * word_length
   
   # Convert target to a list so we can "use up" letters as they are matched
   remaining_letters = list(target)
   
   # First pass: check for correct letters in correct positions
   for i in range(word_length):
      
      if user_guess[i] == target[i]:
         feedback[i] = '*'
         remaining_letters[i] = None
   
   # Second pass: check for correct letters in wrong positions 
   for k in range(word_length):
         if feedback[k] == '-':    
            if user_guess[k] in remaining_letters: 
               feedback[k] = '+' 
               remaining_letters.remove(user_guess[k])  # Prevent reuse
               
   return ''.join(feedback)

# Input validation
def is_valid_length(user_guess):
   return len(user_guess) == word_length

def is_valid_word(user_guess):
   return user_guess in WORDS

def main():
   """
   
   Main game loop:
   - Selects a random word
   - Allows up to 6 guesses
   - Validates input
   - Displays feedback after each guess
   """
   
   target = random.choice(WORDS)
   
   user_guess = ''
   won = False
   print(target)
   print("Welcome to wordle!\n")
   
   for attempt in range(max_attempts):
      user_guess = input('Please enter your word:\n').lower()
      
      if not len(user_guess) == word_length:
         print("Only 5 letter guesses are allowed!")
         continue  
      if not is_valid_word(user_guess):
         print("Invalid word.")
         continue
      
            
            
      result = evaluate_guess(user_guess, target)
         
      
      print(result)
      
      if user_guess == target:
         print("You got it!!")
         won = True
         break
         
   if not won:
      print("You'll get it next time :-).")
   
   print("The correct word was:", target)
    
if __name__ == '__main__':
      main()

    
