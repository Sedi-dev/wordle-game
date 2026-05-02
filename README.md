# 🧩 Wordle Game (Python)

A command-line implementation of the popular Wordle game, built using Python.

The project focuses on logic design, input validation, and interactive gameplay using structured programming.

---

## 🚀 Features

* Random word selection
* Input validation (length + dictionary check)
* Feedback system
     * correct letters
     * correct positions
* Limited attempts system(6 tries)
* Win/lose game states
* Replayable gameplay

---

## 🧠 How the Game Works
- The program selects a random 5-letter word
- The user has 6 attempts to guess the word
- After each guess, feedback is given:
     - * → correct letter in correct position
     - + → correct letter but wrong position
     - - → letter not in word
- The game ends when the word is guessed or attempts run out

---

## 🛠️ Technologies Used

* Python 3

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/Sedi-dev/wordle-game-python.git
```

2. Navigate into the folder:

```bash
cd wordle-game-python
```

3. Run the game:

```bash
python wordle.py
```

---

## 🧠 What I Learned

* How to break down a problem into smaller logical steps
* Designing game logic using conditionals and loops
* Handling and validating user input
* Structuring code using functions for readability
* Working with lists and string manipulation

---

## 🎯 Future Improvements

* Add a graphical user interface (GUI)
* Improve feedback visuals (colours or symbols)
* Expand word list and difficulty levels
* Add scoring system or statistics tracking

---

## 📌 Project Purpose

This project was built to strengthen my understanding of core programming concepts through an interactive and logic-heavy application.

---

⭐️ This project reflects my approach to learning: building real applications to reinforce theoretical concepts.

---

## 👨🏻‍💻 Gameplay Demo 

### Incorrect word/ Word is not valid

<img width="303" height="393" alt="wordle_game_examplerun1" src="https://github.com/user-attachments/assets/605b6f8d-5e4d-45e4-a81c-92eaa9ef3e24" />

### Incorrect word length

<img width="341" height="376" alt="wordle_game_examplerun2" src="https://github.com/user-attachments/assets/bd9d5b0b-ffcd-453e-afbd-dc441c92e2d7" />

###  Correct word

<img width="298" height="262" alt="wordle_game_examplerun3" src="https://github.com/user-attachments/assets/87bfca9d-1d1b-4b67-8e65-07bec5c3ef0b" />
