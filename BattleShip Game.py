#BattleShip Game
import random
import time
print ("Welcome to the game of BATTLESHIP!")
time.sleep(3)
print("There is an enemy battleship lurking near you...")
time.sleep(3)
print("Find it and destroy it before it kills you.\n")
time.sleep(2)
zeros= []
for zero in range(3):#makes 3 lists of Os in list
    zeros.append(['O']*3)#makes 3 zeros in each list
def print_board(zeros):#makes zeros lose the comma and bracket
    for zero in zeros:
        print(" ".join(zero))
print (print_board(zeros))
def turny(w):#returns 3 when turn is 3
  if w ==3:
    print ("The enemy ship avoid your attacks and destorys you with one quick shot!")
    time.sleep(2)
    print ("GAME OVER")
    return int(3)
def row(zeros):
  random_row= random.randint(0, len(zeros)-1)
  return random_row
def column(zeros):#picks random column
  random_column = random.randint(0, len(zeros[0])-1)
  return random_column
ship_row = row(zeros)
ship_column = column(zeros)
for turn in range(4):
  if turny(turn)==3:#turn put into function if turn equals 3 then the function returns 3 and breaks the loop
    break
  else:
    print (f"Turn: {turn+1}\n")
    guess_row= int(input("What row would you like? "))-1 # need minus one because computer starts counting at zero
    guess_column = int(input("What column would you like? "))-1
    if guess_row ==ship_row and guess_column==ship_column:
      print ("CONGRATULATIONS YOU WIN!")
      break
    else:
      if guess_row not in range(3) or guess_column not in range(3):
        print ("You are not aiming properly.")
      else:
        zeros[guess_row][guess_column]= "X"
        print ("You missed")
      
    
    print_board(zeros)