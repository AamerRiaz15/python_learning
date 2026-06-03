# Accumulator Program (main.py)

## Overview
This program repeatedly asks the user to enter numbers and keeps track of three things:
- The running total of all numbers entered
- How many numbers were entered
- The average of the numbers

The program continues accepting input until the user types "done".

## How It Works
1. A `while True` loop keeps the program running.
2. Each input is checked:
   - If the user types "done", the loop ends.
   - If the input is a valid number, it is added to the accumulator.
   - If the input is invalid, the user is asked again.
3. After the loop ends, the program prints:
   - Total of all numbers
   - Average value
   - Number of values entered

## Concepts Practised
- While loops  
- Sentinel values  
- Accumulation patterns  
- Input validation  
- Exception handling with `try` / `except`  

## Example Output
Enter a number or type "done": 10  
Enter a number or type "done": 5  
Enter a number or type "done": done  

Total: 15.0  
Average: 7.5  
Number of values entered: 2
