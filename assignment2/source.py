#!/usr/bin/env python

def main():
  calc()
  guess()
  stack()
  

def calc():
  '''1) Prompt the user to input two numbers and one operator among (+, -, *, /). Depending on the operator, perform the calculation and print the result.'''
  
  #import Decimal
  from decimal import Decimal
  
  #get numbers
  numA = input("Enter first number: ")
  numB = input("Enter second number: ")
  
  #convert to decimal
  try:
    numA = Decimal( numA )
    numB = Decimal( numB )
  except ArithmeticError:
    print( "Input contains errors!" )
    return()
  
  #get operator
  operator = input("Enter operation: ").strip()
  
  #choices
  if operator == "+":
    print(numA + numB)
  elif operator == "-":
    print(numA - numB)
  elif operator == "*":
    print(numA * numB)
  
  #must protect against div/0
  elif operator == "/":
    try:
      print(numA / numB)
    except ArithmeticError:
      print("Can't divide by zero!")
  else:
    print("Unrecognized operator")
  return()

def guess():
  '''2) Write a program to generate a random number(Rnumber) between 1 and 10. (Use randint method from random module). Ask for user to guess a number(Gnumber)
  between 1 and 10. Loop till the user guesses the right number. If Gnumber is less than Rnumber print the message “Your guess is too low”. If Gnumber is greater than Rnumber print the message “Your guess is too high”. Print the total number of guesses. '''
  
  #set up the game
  import random
  correct = random.randint(1,10)
  guess = None
  attempts = 0
  
  while guess != correct:
    attempts += 1
    try:
      guess = int( input( "Enter a guess: " ) )
    except ValueError:
      print("Not even close.")
      continue
    
    #outside the bounds of the game
    if guess not in range(0,10):
      print("Try guessing numbers between 1 and 10")
      continue
    
    #too high / low
    if guess > correct: print("Your guess is too high!")
    if guess < correct: print("Your guess is too low!")
  
  #if correct number guessed
  print("Correct! Wow! First guess!") if attempts == 1 else print("Correct! You used {} guesses!".format(attempts) )


def stack():
  '''3) Implement stack(First In First Out) using list with below operations.
  a) Ask the user choice – push, pop OR quit
  b) If push, add the value entered by the user and display the new list.
  c) If pop, display the element popped and the new list.
  d) Push/Pop operations to be carried out till the user quits'''
  
  #set up the data storage
  storage = []
  
  #set up the loop
  while True:
    #get user command
    command = str( input("(A)ppend / (R)emove / (Q)uit: ") )
    
    if command.lower() == "a":
      #then append
      storage.append( input("Enter value: " ) )
      showStorage(storage)
    
    elif command.lower() == "r":
      #then pop
      print("Removed item: {}".format( storage.pop(0) ) ) if storage else print("Can't pop from empty stack")
      showStorage(storage)
    
    else:
      #assume quit
      print("Quitting!")
      return()

def showStorage(storage):
  '''Output the storage list'''
  if not storage:
    print("Stack is empty")
  else:
    print(storage)

if __name__ == '__main__':
  main()

