def tshop(Coins):
  print("You reach the blacksmith's")
  print("BlackSmith:Sorry Kid,this sword is the only thing available today")
  print("You Great!")
  input()
  while True:
    if input("press 1 to buy the sword for 5 coins.")==1:
      Coins =- 5
      print("Sword bought!")
      print("you now have "+str(Coins)+" coins")
      return -5
    else:
      print("Sorry, that was not a available input")
      print()
      
def tshop(Coins):
  input()
  while True:
    print("to buy an item press press the number")
    print("1=sword(costs 5 coins) 2=health potion(costs 2 coins)")
    input()=id
    if id ==1:
      Coins =- 5
      print("Sword bought!")
      print("you now have "+str(Coins)+" coins")
      return -5
    elif id ==2:
      Coins =- 2
      print("Sword bought!")
      print("you now have "+str(Coins)+" coins")
      return -2
     else:
      print("Sorry, that was not a available input")
      print()
      
