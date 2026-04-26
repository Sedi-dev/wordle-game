#Wordle Clone(python)
A simple but fully functional Wordle-style word guessing game built in python.
This projects simulates the core mechanics of the popular game, including letter matching logic, input validation, and limited attempts.

---

## 📌 Project Overview

This program selects a random 5-letter word from a dictionary file and challenges the user to guess it within 6 attempts.

After each guess, the game provides feedback using symbols:
- '*' → Correct letter in the correct position
- '+' → Correct letter in the wrong position
- '-' → Letter not in the word

---

## ⚙️ Features
- Random 5-letter word selection from a word list file
- Input validation (5-letter word check)
- Wordle-style feedback system (position + presence checking)
- File-based dictionary ('words.txt')
- Limited 6-attempt gameplay system
- Win/Lose detection

---

## 🧠 Key Concepts Demonstrated

This project demonstrates understanding of:

- Python loops and conditionals
- String manipulation
- File handling
- Lists and iteration
- Algorithm design (two-pass matching system)
- Input validation
- Game logic implementation

---  

## ▶️ How to Run the Project
1. Ensure Python is installed on your system
2. Download or clone this repository
3. Make sure 'words.txt' is in the same folder as 'wordle.py'
4. Run the program:

---

## 💡 Learning Outcome

Through this project, I have developed a deeper understanding of algorithm design, particularly handling edge cases such as repeated letters and accurate feedback generation.

🚀 Future Improvements
~ Add a graphical user interface (GUI)
~ Track player statistics (wins/losses)
~ Implement difficulty levels

```bash
python wordler as 'wordle
