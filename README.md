# 🎰 Slot Machine Game (Python)

A simple console-based slot machine game written in Python.  
Players can place bets on multiple lines and spin the reels to try their luck winning payouts based on matching symbols.

---

## Features
- Supports betting on 1 to 3 lines  
- Customizable bet amounts per line with limits  
- Randomly generates slot reels with weighted symbol frequencies  
- Calculates winnings based on matched symbols on active lines  
- Displays the slot reels in a readable column-row format  
- Keeps track of player balance and allows multiple spins until quitting  

---

## How to Play
1. Run the script in a Python 3 environment.  
2. Deposit an initial amount of money to start playing.  
3. Choose the number of lines you want to bet on (1 to 3).  
4. Choose how much you want to bet per line within allowed limits.  
5. Spin the slot machine and see if you win!  
6. Continue playing until you decide to quit or run out of money.  

---

## Code Structure Overview

- `symbol_count`: Dictionary defining the number of each symbol on the reels (controls frequency).  
- `symbol_value`: Dictionary defining payout multipliers for each symbol.  
- `get_slot_spin(rows, cols, symbols)`: Generates a random spin of the slot reels.  
- `print_slot_machine(columns)`: Prints the reels visually in the console.  
- `check_winnings(columns, lines, bet, values)`: Calculates winnings and winning lines.  
- User input functions:  
  - `deposit()`: Gets starting balance.  
  - `get_number_of_lines()`: Gets how many lines to bet on.  
  - `get_bet()`: Gets bet per line.  
- `spin(balance)`: Runs a single spin, updates balance.  
- `main()`: Runs the game loop until user quits.

---

## Requirements
- Python 3.x  
- No external libraries required (uses built-in `random` module)

---

## Usage
Run the script in a terminal or command prompt:

```bash
python slot_machine.py
