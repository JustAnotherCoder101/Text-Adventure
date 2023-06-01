def tshop(Coins):
  print("You reach the blacksmith's")
  input
  print("BlackSmith:Sorry Kid,this sword is the only thing available today")
  input
  print("You:That's all I need")
  input()
  while True:
    if input("press 1 to buy the sword for 5 coins.")=="1":
      Coins =- 5
      print("Sword bought!")
      print("you now have "+str(Coins)+" coins")
      return "Sword1"
    else:
      print("Sorry, that was not a available input")
      print()
      
def shop(Coins):
  input()
  while True:
    print("to buy an item press press the number")
    print("1=sword(costs 5 coins) 2=health potion(costs 2 coins)")
    id = input()
    if id =="1":
      Coins =- 5
      print("Sword bought!")
      print("you now have "+str(Coins)+" coins")
      return "SwordLv2"
    elif id =="2":
      Coins =- 2
      print("Sword bought!")
      print("you now have "+str(Coins)+" coins")
      return "HP1"
    else:
      print("Sorry, that was not a available input")
      print()
      
