
# PYTHON QUIZ GAME

A simple command-line quiz game written in Python. It presents a set of multiple-choice questions about Python, randomizes their order, and evaluates your answers at the end.

## Features

- 5 multiple-choice questions about Python programming
- Questions are shuffled (randomized) on every run
- User inputs answers as `A`, `B`, or `C` (case-insensitive)
- Instant feedback after each answer (correct or wrong)
- Final score displayed out of the total number of questions
- Personalized result message based on your score

## Requirements

- Python 3.x
- No external libraries required (uses only the built-in `random` module)

## How to Run

Run the game from the command line:

```bash
python quiz.py
```

## How to Play

1. When the game starts, a question is displayed along with three options (A, B, C).
2. Type your answer as `A`, `B`, or `C` and press **Enter**.
3. The game tells you whether your answer is correct or wrong.
4. After all questions are answered, your final score is shown along with a result message.

## Questions in the Quiz

| # | Question | A | B | C | Correct |
|---|----------|---|---|---|---------|
| 1 | Which language are we learning? | Python | Java | C++ | A |
| 2 | What is 5 + 3? | 8 | 10 | 15 | A |
| 3 | Which function displays output? | input() | print() | int() | B |
| 4 | Which symbol is used for comments? | # | // | $ | A |
| 5 | Which data type stores True or False? | int | str | bool | C |

*Note: Because questions are shuffled, the order they appear in each game will be random.*

## Scoring

- You get **1 point** for each correct answer.
- Your final score is shown as `Your score: X out of 5`.

Result messages:

- **Excellent!** — answered all questions correctly
- **Good job!** — scored 3 or more
- **Keep practising!** — scored less than 3
