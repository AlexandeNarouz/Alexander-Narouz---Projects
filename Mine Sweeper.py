import time
import random
listo=[]
print ("WELCOME TO DEADLY MINE FIELD.\n")
time.sleep(2)
print("Avoid the mines.")
print("Goodluck!\n")
time.sleep(3)
for zero in range(5):
    listo.append(['O']*5)
def print_listo(listo):
    for zero in listo:
        print (" ".join(zero))
print (print_listo(listo))
def random_row(l):
    random_row= random.randint(0, len(listo)-1)
    return random_row
def random_column(l):
    random_column= random.randint(0, len(listo[0])-1)
    return random_column
mine1_row = random_row(listo)
mine1_column = random_column(listo)
mine2_row = random_row(listo)
mine2_column = random_column(listo)
mine3_row = random_row(listo)
mine3_column = random_column(listo)
mine4_row = random_row(listo)
mine4_column = random_column(listo)
mine5_row = random_row(listo)
mine5_column = random_column(listo)
mine6_row = random_row(listo)
mine6_column = random_column(listo)
count= 0
linga = True
while count <11 and linga==True:
    if count==10:
        print ("CONGRATULATIONS ON WINNING!")
        linga ==False
        break
    else:
        print (f"You are safe for {count} steps so far...\n")
        row= int(input("What row would you like to walk?: "))-1
        column= int(input("What column would you like to walk?: "))-1
        if row==mine1_row and column==mine1_column or row==mine2_row and column==mine2_column or row==mine3_row and column==mine3_column or row==mine4_row and column==mine4_column or row==mine5_row and column==mine5_column or row==mine6_row and column==mine6_column:
           print(" ")
           print ("You stepped on a mine and blew up!")
           print ("GAME OVER")
           print (f"You made it {count} steps!")
           linga ==False
           break
        else:
            time.sleep(1)
            print ("You are safe.")
            listo[row][column]= 'x'
            count+=1
    print_listo(listo)
    
    