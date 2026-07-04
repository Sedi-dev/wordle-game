# 🧩 Wordle Game (Python)

A command-line implementation of the popular Wordle game built in Python.

This project was developed to strengthen my understanding of algorithm design, problem decomposition, and user input validation through an interactive terminal-based game.

---

## Project Overview

The Wordle game challenges the user to guess a randomly selected 5-letter word within 6 attempts. After each guess, the program provides feedback to help the user refine their next attempt.

This project focuses on:

* Breaking down a real-world problem into logical steps
* Implementing a structured algorithm for letter matching
* Handling user input and validation safely
* Writing clean, modular Python code

---

## Features

* Random selection of a valid 5-letter word
* Limited attempts system (6 guesses)
* Input validation (length + dictionary check)
* Wordle-style feedback system:
  * `*` → correct letter in correct position
  * `+` → correct letter in wrong position
  * `-` → letter not in word
* Handles duplicate letters correctly
* Clear win/lose game states

---

## How It Works (Core Logic)

The feedback system uses a **two-pass matching algorithm**:

1. First pass:

   * Identifies letters in the correct position (`*`)
   * Marks them as used

2. Second pass:

   * Checks for correct letters in wrong positions (`+`)
   * Prevents reuse of already matched letters

This ensures accurate feedback even when duplicate letters exist in the word.

---

## Technologies Used

* Python 3
* Built-in `random` module
* File handling (`words.txt` word list)

---

##  Dependencies
No external libraries required. Python standard library only.

### Word List Source
The repository includes `words.txt` containing all valid 5-letter words. 
The game reads from this file automatically — no additional setup needed.

---

## Project Structure

```
wordle-game/
│
├── wordle_game.py        # Main game logic
├── words.txt        # Valid word list
└── README.md
```

---

## How to Run

Clone the repository:

```bash id="run1"
git clone https://github.com/Sedi-dev/wordle-game.git
```

Navigate into the project folder:

```bash id="run2"
cd wordle-game
```

Run the game:

```bash id="run3"
python wordle_game.py
```

---

## What I Learned

* How to design an algorithm for pattern matching
* How to structure a program using functions
* How to validate and sanitize user input
* How to manage game state using loops and conditions
* How to handle edge cases like duplicate letters

---

## Challenges Faced

One of the main challenges in this project was correctly handling duplicate letters in the target word. This was solved by tracking remaining unmatched letters and using a two-pass evaluation system.

---

## Future Improvements

* Add difficulty levels (easy / hard modes)
* Create a GUI version using Tkinter or a web interface
* Add scoring system and win statistics
* Improve word list filtering and loading performance

---

## Project Purpose

This project was built as part of my learning journey in Computer Science to apply theoretical programming concepts in a practical, interactive application.

It demonstrates my ability to:

* Break down problems logically
* Build working software from scratch
* Write structured and maintainable code

---

⭐ If you found this project interesting, feel free to explore my other repositories.

---

## Gameplay Demo 

### Invalid word
![Incorrect word/ Word is not valid](https://github.com/user-attachments/assets/1887fb21-5396-4f52-a552-c61af3d60001)


### Invalid word length
![Incorrect word length](https://github.com/user-attachments/assets/981e89ae-9d65-4721-96fb-2509167caaa6)


### Correct word
![Correct word](https://github.com/user-attachments/assets/18a9cb98-b53b-4b1b-9d74-024428303713)


