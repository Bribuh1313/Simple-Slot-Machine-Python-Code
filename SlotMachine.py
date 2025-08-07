#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 14:49:58 2025

@author: briannamerila
"""

import random # This will readomly generate slot machine values

MAX_LINES = 3 #This is a constant non changing value 
MAX_BET = 100
MIN_BET = 1

#Rows and columns for slot machine
rows = 3
cols = 3

#Symbols on reel(column)
symbol_count = { #{} makes a library
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8}

symbol_value = { #{} makes a library
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] 
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line +1)
    return winnings, winning_lines
    
    
def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = [] #all of the nested lists will represent the value in the column
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #this is a slice operator [:] that will create a copy of the object
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) #This will get rid of teh first instance in the list so it does not pick it again
            column.append(value)
            
        columns.append(column) #This will store the found random values from the loop above and store it in the columns list above
        
    return columns
    
def print_slot_machine(columns): #this will loop thri\ough every row for each column and it will transpose the columns to be vertical
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
                
        print()
    
#setting the bet
def deposit():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():#makes sure that the input from the user is a digit and not a string 
            amount = int(amount) #converts to number
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.") #this will show up if they dont enter a number
    return amount

#collecting the bet
def get_number_of_lines():
    while True:
        lines = input("Enter number of lines you are betting on. (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():#makes sure that the input from the user is a digit and not a string 
            lines = int(lines) #converts to number
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.") #this will show up if they dont enter a number
    return lines

# How much to bet on each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():#makes sure that the input from the user is a digit and not a string 
            amount = int(amount) #converts to number
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.") #this will show up if they dont enter a number
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet, your current balance is: ${balance}")
        else:
            break
    
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_spin(rows, cols, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"you won on line:", *winning_lines)
    
    return winnings - total_bet

def main(): #if we end the program, we can call main and it will run again
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
main()

