import function
import time
import random
Coins=10
Inventory = []
print("You are strolling through the unexplored,dense forrest")
time.sleep(1)
input("press enter to continue")
print("You have found a strange looking house")
input()
if input("go in to the house?(type 1 for yes type 2 for no)")==1:
  print("you walk away and go about your life.")
  time.sleep(1)
  print("THE END.")
  exit()
print("You enter the strange looking house")
input()
print("Old Man:What are you doing here!")
input()
print("You:I didn't know anyone lived here.")
input()
print("Old Man:Well...")
input()
print("Old Man:I'm sorry for getting cranky at ya,")
input()
print("Old Man:You never know who can be lurking...")
input()
print("Old Man:Would you like to learn some skills?")
input()
print("You:Okay?")
input()
print("Old Man: have 5 coins to by yourself a sword and come back here to train")
input()
print("You:.. Thanks?")
input()
Coins += 5
print("+5 coins!")
input()
print("You now have "+str(Coins)+" coins")
input()
print("You walk out of the forrest and to the blacksmith's shop")
print()
time.sleep()
print("As You walk out of the forrest you don't feel right...")
print()
time.sleep(0.5)
print()
print("you think you hear somthing but look back and find nothing")
time.sleep(0.5)
print()
print('"It was probably nothing" you say but you know somthing was off..')
input()
Coins= Coins + function.tshop(Coins)




