# Python Slot Machine

A simple console-based slot machine game built with Python.

This project was created to practice Python fundamentals such as functions, loops, dictionaries, input validation, randomization, and basic game logic.

## Features

- 3x3 slot machine
- Random symbol generation
- Multiple betting lines
- Minimum and maximum bet limits
- Balance tracking
- Input validation
- Winning line detection
- Different payout values for each symbol
- Prevents users from betting more than their available balance
- Allows the user to keep spinning until they choose to exit or run out of money

## How It Works

The user starts by entering a deposit amount.

They can then choose:

1. How many lines they want to bet on
2. How much they want to bet on each line

The program generates a random 3x3 slot machine result and checks each selected line for matching symbols.

If all symbols on a selected line match, the user receives a payout based on the symbol's value and their bet amount.

The user's balance is updated after every spin.

## Technologies Used

- Python
- Python `random` module

## Concepts Practiced

- Functions
- Loops
- Conditional statements
- Dictionaries
- Lists
- Input validation
- Randomization
- Constants
- Game state and balance tracking

## Running the Project

Make sure Python is installed.

Clone the repository and run:

```bash
python slots_project.py
```

## Example

```text
How much cash would you like to deposit? $100

Current balance is $100
Press ENTER to spin! (Type EXIT to quit):

Enter the number of lines to bet on (1-3)? 2
How much would you like to bet on each line? You have $100 remaining: $10

You are betting $10 on 2 lines. Your total bet is $20.

A | B | D
A | A | A
D | C | B

You won $50!
You won on line(s): 2
```

## Purpose

This was one of my earlier Python projects and helped me strengthen my understanding of breaking a program into smaller functions, validating user input, working with collections, and managing program state.