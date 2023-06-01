import function
import time
import random

Coins = 10
Inventory = []
Lvl = 1
XP = 0
XPLvl = 20
Name = ""
print("You are strolling through the unexplored,dense forrest")
input()
input("press enter to continue")
print("You have found a strange looking house")
input()
if input("go in to the house?(type 1 for yes type 2 for no)") == "2":
  print("you walk away and go about your life.")
  print("THE END.")
  input()
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
print(
  "Old Man: have 5 coins to by yourself a sword and come back here to train")
input()
print("You:.. Thanks?")
input()
Coins += 5
print("+5 coins!")
input()
print("You now have " + str(Coins) + " coins")
input()
print("You walk out of the forrest and to the blacksmith's shop")
print()
input()
print("As You walk out of the forrest you don't feel right...")
print()
input()
print()
print("you think you hear somthing but look back and find nothing")
input()
print()
print('"It was probably nothing" you say but you know somthing was off..')
input()
function.tshop(Coins)
Coins -= 5
Inventory.append("SwordLvl1")
print("You put your basic sword into your empty backpack and head off")
input()
print("You go back through the forrest,to the man then into the house")
input()
print("Old Man: Oh, hello there.")
input()
print("You:So, I've guess will I be training in combat? ")
input()
print("Old Man: Yes yes.... Wait!")
input()
print("You: What?")
input()
print("Old Man: I'm just joking with ya but i need to ask your name")
print()
while True:
  Name = input("Old Man: What is it?")
  if Name == "" or Name == " ":
    print("Old Man: Speak up young chap!")
  else:
    break
print("You: My name is " + Name)
input()
print("Old Man: Well, Nice to meet you " + Name + " My name is Dave")
